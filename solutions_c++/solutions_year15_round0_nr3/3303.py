#include<bits/stdc++.h>
#include <fstream>

using namespace std;
 
#define ll long long int
#define ull unsigned long long int
#define maxN 100005
#define logN 18
#define maxW 1005
#define MOD 1000000007
#define pb push_back
#define mp make_pair
#define INF (((ll)1000000000) * ((ll)1000000000))
#define e 2.7182818284590452353602874
#define maxT 100000

int A[10][10]={ {0,0,0,0,0} , {0,1,2,3,4} , {0,2,-1,4,-3} , {0,3,-4,-1,2} , {0,4,3,-2,-1} };

int S[100005],fp[100005],rp[100005];

int mul(int i,int j) {
 if(i==0)
  return j;
 if(i*j>0)
  return A[abs(i)][abs(j)];
 else
  return -A[abs(i)][abs(j)]; 
}

int main() {

ifstream infile("thefile.txt");
ofstream mf;

int T;
infile>>T;
cout<<T<<"\n";

for(int tc=1;tc<=T;tc++) {

int L,X;
infile>>L>>X;

string s;
infile>>s;

string ss;
ss.clear();

while(X--)
ss+=s;

int N=ss.size();

for(int i=0;i<ss.size();i++)
if(ss[i]=='1')
S[i]=1;
else if(ss[i]=='i')
S[i]=2;
else if(ss[i]=='j')
S[i]=3;
else
S[i]=4;

/*
for(int i=0;i<N;i++)
cout<<S[i];
cout<<"\n";
cout<<ss<<"\n";*/


fp[0]=S[0];
for(int i=1;i<N;i++) {
fp[i]=mul(fp[i-1],S[i]);
}

/*
for(int i=0;i<N;i++)
cout<<fp[i]<<" ";
cout<<"\n";
*/

rp[N-1]=S[N-1];
for(int i=N-2;i>=0;i--) {
 //cout<<"multiplying "<<S[i]<<" "<<rp[i+1]<<"\n";
 rp[i]=mul(S[i],rp[i+1]);
}

/*
for(int i=0;i<N;i++)
cout<<rp[i]<<" ";
cout<<"\n";*/

bool pos=false;

for(int i=0;i<N;i++){
//cout<<"for index "<<i<<"\n";
	if(fp[i]==2) {
 	//cout<<"\nmaybe for index "<<i<<"\n";
  		int p=0;
  		for(int j=i+1;j<N;j++) {
   			p=mul(p,S[j]);
			//cout<<p<<" ";
   				if(p==3 && rp[j+1]==4) {
					//cout<<"maybe j for index "<<j<<"\n";
    					pos=true;
    					break;
   				}
  			}

 	if(pos)
  	break;
 	} 
}

string ans;
if(pos)
ans="YES";
else
ans="NO";



cout<<"Case #"<<tc<<": "<<ans<<"\n";

}

mf.close();

return 0;
}
