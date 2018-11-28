#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <cmath>
#include <vector>
#include <algorithm>

#define MAX 4
#define test(a) cout << "TEST " << a << endl;

using namespace std;

void strtovec(vector<int>& v, string s){
    for (int a=0; a<s.size(); a++){
        v[a]=(s[a]-'0');
    }
}

bool lessorequalto(vector<int> v, vector<int> u ){
    if(v.size()<u.size()){
        return true;
    }
    if(v.size()>u.size()){
        return false;
    }
    for(int a=0; a<v.size(); a++){
        if(v[a]<u[a]) return true;
        if(v[a]>u[a]) return false;
    }
    return true;
}

bool palindromic(vector<int> v){
    for(int a=0; a<(v.size()+1)/2; a++){
        if(v[a]!=v[v.size()-1-a]){
            return false;
        }
    }
    return true;
}

bool allonedigit(vector<int> v){
    for(int a=0; a<(v.size()+1)/2; a++){
        if(v[a]>=10){
            return false;
        }
    }
    return true;
}

bool squaregood(vector<int> v, vector<int> start, vector<int> end){
    if(palindromic(v)){
        //cout << "THERE" << endl;
        vector<int> square(2*v.size()-1, 0);
        for(int a=0; a<square.size(); a++){
            int total=0;
            for(int b=max(0, (int) (a-v.size()+1));b<=min(a, (int) v.size()-1); b++){
                total+=v[b]*v[a-b];
            }
            square[a]=total;
        }
        if(lessorequalto(start, square)){
            if(lessorequalto(square, end)){
                if(allonedigit(square)){
                   return true;
                }
            }
        }
    }
    return false;
}

int singles(vector<int> start, vector<int> end){
    int total=0;
    if(start.size()==1){
        if(start[0]<=9&&(end.size()>1 || end[0]>=9)) total++;
    }
    return total;
}

int threes(int n){
    int total=0;
    while(n%3==0){
        n/=3;
        total++;
    }
    return total;
}

void display(vector<int> v) {
    for (int n=0; n<v.size(); n++) {
        cout << v[n] << " ";
    }
    cout << "\n";
}

int doubles(vector<int> start, vector<int> end){
    int total=0;
    int s=(start.size()/2)+1, e=(end.size()+1)/2;
    //cout << "s="<< s <<" e=" << e <<endl;
    vector<int> v(10,0);
    for(int a=s;a<=e; a++){
        //cout << "a=" << a << endl;
        v.resize(a);
        v[0]=1;
        for(int b=1; b<v.size()-1; b++){
            v[b]=0;
        }
        v[v.size()-1]=1;
        if(squaregood(v,start, end)){
            total++;
            //display(v);
        }
        for(int b=1; b<2*(pow(3,((int) ((a-1)/2)))); b++){
            //cout << "b=" << b << endl;
            if(a%2==1){
                if(threes(b)!=0){
                v[(a-1)/2+threes(b)]=(v[(a-1)/2+threes(b)]+1)%3;
                v[(a-1)/2-threes(b)]=(v[(a-1)/2-threes(b)]+1)%3;
                }
                else{
                v[(a-1)/2]=(v[(a-1)/2]+1)%3;
                }
            }
            if(a%2==0){
                v[a/2+threes(b)]=(v[a/2+threes(b)]+1)%3;
                v[a/2-threes(b)-1]=(v[a/2-threes(b)-1]+1)%3;
            }
            //cout << "HERE" << endl;
            if(squaregood(v,start, end)){
                total++;
                //display(v);

            }
        }
    }
    return total;
}

int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int cases, total;
    fin >> cases;
    //test(1)
    vector<int> start(1,0);
    vector<int> end(1,0);
    for(int a=1; a<=cases; a++){
        string s, e;
        int test;
        fin >> s >> e;
        //test(2)
        start.resize(s.size());
        end.resize(e.size());
        strtovec(start, s);
        strtovec(end, e);
        total=0;
        //test(3)
        total+=singles(start, end);
        //cout << "Case #"<< a <<" SINGLES: " << singles(start, end) << endl;
        //test(4)
        total+=doubles(start, end);
        //cout << "Case #"<< a <<" DOUBLES: " << doubles(start, end) << endl;
        //test(5)
        //cout << a << endl;
        fout << "Case #"<< a <<": " << total << endl;
    }


}
