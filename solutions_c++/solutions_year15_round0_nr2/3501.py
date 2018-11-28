#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <map>
#include <vector>

using namespace std;

vector<int> a(1200,0) ;  
int max1 = 0;
int min1;

void solve(map<int, int, greater<int> > &m, int &res, int stoptimes){
    if(m.size()==0) { res = -2;return;}
    if(m.find(0)!=m.end()) {res = -1; return;}
    if(m.size()==1&&m.find(1)!=m.end()){
        res = min(res,m[1]+stoptimes);
        return;
    }
    res = min(res, m.begin()->first + stoptimes);
    //split
    int value = m.begin()->second;
    stoptimes += value;
    int left = (m.begin()->first)/2;
    int right = (m.begin()->first)-left;
    m.erase(m.begin());
    if(m.find(left)==m.end()) m[left]=0;
    if(m.find(right)==m.end()) m[right]=0;
    m[left]+=value;
    m[right]+=value;
    solve(m,res,stoptimes);
}

int main(){
    long long res;
    ifstream myfile;
    myfile.open("B-large.in.txt");
    ofstream outfile;
    outfile.open("output.txt");
    string line;
    getline(myfile,line);
    const int t=atoi(line.c_str());
    for(int i=0;i<t;i++){
        getline(myfile,line);
        istringstream iss(line);
        string str;
        iss>>str;
        int k = atoi(str.c_str());
        getline(myfile,line);
        istringstream iss2(line);

        map<int, int, greater<int> > m;
        for(int j=0;j<k;j++){
            iss2>>str;
            int v = atoi(str.c_str());
            cout<<" "<<v;
            if(m.find(v)==m.end()) m[v]=0;
            m[v]++;
a[j]=v;
max1=max(max1,v);


        }
        // for(auto iter=m.begin();iter!=m.end();iter++){
        //     cout<<endl<<iter->first<<" "<<iter->second;
        // }
        int res = INT_MAX;
        solve(m,res,0);
        // cout<<endl<<"res: "<<res;
        cout<<endl;
        if(res<0) cout<<res<<" Error In Line: #"<<i+1<<endl;
        if(res==INT_MAX) cout<<res<<" Error In Line: #"<<i+1<<endl;
        // outfile<<"Case #"<<(i+1)<<""<<": "<<res<<endl;
        cout<<"Case #"<<(i+1)<<""<<": "<<res<<endl;



min1 = max1;
        for(int i = 1 ; i <= max1 ; i++) {  
            int sum = i ;  
            for(int j = 0 ; j < k ; j++) {  
                if( a[j] > i ) {  
                    if( a[j]%i == 0 )  
                        sum += (a[j]/i-1) ;  
                    else  
                        sum += (a[j]/i) ;  
                }  
            }  
            min1 = min(min1,sum) ;  
        }  
        printf("!!!Case #%d: %d\n", i+1, min1) ;  
        if(res!=min1) cout<<"!!!!!!!!!!!!!!!!!!!!!!!!!!"<<endl;

        res=min(res,min1);
        outfile<<"Case #"<<(i+1)<<""<<": "<<res<<endl;




    }

    outfile.close();
    myfile.close();
    return 1;
}














