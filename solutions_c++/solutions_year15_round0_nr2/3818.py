#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <iterator>
#include <time.h>
#include <map>
#include <thread>

#define ulint unsigned long int
using namespace std;



//***********************************************************************************************
//***********************************************************************************************
//***********************************************************************************************
//Helpers:

//simple split according to a delimitor.
std::vector<std::string> &split(const string &s, char delim, vector<string> &elems) {
    std::stringstream ss(s);
    std::string item;
    while (std::getline(ss, item, delim)) {
        elems.push_back(item);
    }
    return elems;
}


template< class T >

void display_vect(vector <T> v) {
    for(auto& it : v) {
        cout << it <<" ";
    };
    cout << endl;
}


//Simple check if s is in v
bool is_in(vector<ulint> v,ulint s){
    return (find (v.begin(),v.end(),s) != v.end());
}

// /Helpers.
//***********************************************************************************************
//***********************************************************************************************
//***********************************************************************************************


class ToSolve{
  private:
    vector<int> pancakes;

  public:
    string solution;
    void fill(vector<int> v_) {pancakes=v_;}
    void getsolution();

};



tuple<int,int,int> maxelems(vector<int> v){
    int count=0;
    int maxi=*max_element(v.begin(),v.end());
    int snd_max=0;
    for (auto& it : v){
        if (it==maxi) count++;
        if (it>snd_max && it<maxi){snd_max=it;};
    }
    return make_tuple(maxi,count,snd_max);
}

vector<int> special_minutes(vector<int> v,int max){
    vector<int> res= v;
    for (ulint i=0;i<v.size();i++){
        if (v.at(i)==max)
            {res.at(i)=max/2+(max % 2);
             res.push_back(max/2);}
    }
    return res;
}

vector<vector<int>> special_minutes_iter(vector<int> v,int max){
    vector<vector<int>> res;
    for (ulint i=0;i<v.size();i++){
        if (v.at(i)==max)
        {for(int j=1;j<=max/2;j++){
             vector<int> temp=v;

             temp.at(i)=max-j;
             temp.push_back(j);
             res.push_back(temp);
             }
             break;}
    }
    return res;
}

void normal_minute(vector<int> &v){
    for(auto &it : v) {it=max(0,it-1);}
}

void ToSolve::getsolution() {
    tuple<int,int,int> maxis=maxelems(pancakes);
    int curr=get<0>(maxis); // contains current upper bound;
    int num=get<1>(maxis); // contains current number of maxi plates;
    int snd_max=get<2>(maxis);
    int count=curr;
    int maxi;
    int n=0;
    vector<vector<int>> pancakes_= {pancakes};
    vector<vector<int>> res;
    while(n<curr){
            res=pancakes_;
            for (ulint i=0;i<pancakes_.size();i++){
                maxi=*max_element((pancakes_.at(i)).begin(),(pancakes_.at(i)).end());
                if ((maxi<=0) && n<count) {count=n;}
                vector<vector<int>> v=special_minutes_iter((pancakes_.at(i)),maxi);
                res.insert(res.end(),v.begin(),v.end());
                normal_minute(res.at(i));
            }
            pancakes_=res;
            n++;
    }

    solution=to_string(count);
}


/*
void ToSolve::getsolution() {
    tuple<int,int,int> maxis=maxelems(pancakes);
    int curr=get<0>(maxis); // contains current upper bound;
    int num=get<1>(maxis); // contains current number of maxi plates;
    int snd_max=get<2>(maxis);
    int count=0;
    vector<int> pancakes_=pancakes;
    while(num+max((curr/2) +(curr % 2),snd_max) <= curr){
        if (curr%2==0) {pancakes_=special_minutes(pancakes_,curr);}
        else           {normal_minute(pancakes_);
                        num=1;}
    count+=num;
    maxis=maxelems(pancakes_);
    curr=get<0>(maxis);
    num=get<1>(maxis);
    snd_max=get<2>(maxis);
    }
    count+=curr;
    solution=to_string(count);
}
*/

// To Parallelize the tests cases:
void compute_atom(vector<ToSolve> &v,ulint n_core,ulint curr){
    for(ulint i=0;i<v.size();i++){
        if ((i % n_core) == curr)(v.at(i)).getsolution();
        if (curr==0 && i % max({(ulint) 1,(v.size()/10)})==0 )
                                    cout<< ((i*100)/v.size())<<"% done"<<endl;
    }
}

void computePar(vector<ToSolve> &v,ulint n_core){
    vector<thread> threads;
    for(ulint i = 0;i<n_core;i++){
        threads.push_back(thread(compute_atom,ref(v),n_core,i));
    }
    for(auto & it : threads){
        it.join();
    }
}


int main()
{
    string n_str;
    ulint n;
    time_t timer,timer_fin;
    time(&timer);
    ifstream infile;
    ofstream outfile;
    
    infile.open("test.in");
    outfile.open("test.out");
    
    getline(infile,n_str);
    n=stoul(n_str);

    cout << n << endl;

    //

    vector<ToSolve>cases(n);
    // where we parse the problems:
    for (auto& it : cases){
        vector<string> v;
        string line0;
        getline(infile,line0);
        string line1;
        getline(infile,line1);
        split(line1,' ',v);
        vector<int> v_;
        for(auto& it : v) v_.push_back(stoi(it));

        it.fill(v_);

    };
    // where we compute the solutions
    //one one thread:
        //for (auto& it : cases) it.getsolution();
    //in par
    computePar(cases,min({(long unsigned int)7 , n}));
    // the above could be parellised


    //we save the cases solutions
    int i = 0;
    for (auto& it : cases){
        outfile << "Case #" << i+1 <<": ";
        outfile << it.solution << endl;
        i++;
    };

    infile.close();
    outfile.close();
    time(&timer_fin);
    cout<<"Done in "<<difftime(timer_fin,timer)<<" s"<<endl;

    return (0);
}



