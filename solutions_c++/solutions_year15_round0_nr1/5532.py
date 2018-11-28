#include<stdio.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<string.h>
#include<vector>
#include<memory.h>
#include<cassert>
#define lint long long
#define rep(i,a,b) for(int i=a; i<b; i++)
#define p_b(V,x) V.push_back(x)
#define sc(x) scanf("%d", &x)
#include<fstream>
using namespace std;
int main(){
	int k=1;
    int t;
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    fin>>t;
    while(t--){
        int n;
        fin>>n;
        n++;
        fin.ignore();
        string str;
        getline(fin,str);
        lint cnt=str[0]-'0';
        //cout<<str<<" "<<cnt<<endl;
        lint ans=0;
        rep(i,1,n){
            int j = str[i]-'0';
            if(cnt<i){
                ans+=i-cnt;
                cnt=i+j;
            }
            else cnt+=j;
        }
        fout<<"Case #"<<k<<": "<<ans<<endl;
        k++;
    }
}
