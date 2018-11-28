#include<bits/stdc++.h>
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <iterator>
#include <ctype.h>
#include <algorithm>
#include<vector>
#include<cmath>
#include <iomanip>
#include <string>
#include <sstream>
#include <cstring>
//void print(const char* input)
bool prime( long long int );
#define FOR(i,N) for(int i=0;i<(N);i++)
std::vector<long int> vec;
 long long  int j=0,jj,c1=0,c0=0;
int cas=1;
std::string s;
std::string::size_type sz = 0;
using namespace std;

FILE *f,*f1;
//std::ofstream out("*.txt");
void printvec(std::string , vector<long int> v);
bool ck=false;
void printall(char arr[], char temp[], int i, int k, int n) {
    if(j<jj)
    {
    s="";
	if(i == k) {
		FOR(m, k)
		{
       //  if(temp[m]=='1')
		 s=s+temp[m];
		}
		//cout <<s<<endl;
		long int l=s.length();
        //
      //   long long ull = std::stoull (str,&sz,0);
		if(s[0]=='1'&& s[l-1]=='1')
            {
         // cout<<"  yes \n"<<endl;
          //  c1++;
            std::string str = s;
            long long int iin = std::stoull (str,&sz,10);

          //  fprintf(f1," Base= %d", i)
            for(i=2;i<=10;i++)
            {
           //  fprintf(f1," String = %d  Base= %d  /n",iin,i);
           //long long int i_int = std::stoll (str,nullptr,i);
            ck=false;
            long long int ull = std::stoull (str,&sz,i);
           cout<< "string = "<<iin<<" base = "<<i<<" i_int = "<<ull<<endl;
            ck=prime(ull);
            if(ck==false)
                {
                s="";
                vec.clear();
                break;

                }
            }
           if(ck==true)
                printvec(s,vec);



	}
    return;
	}
	FOR(p, n) {
		temp[i] = arr[p];
		//cout<<"\n Inside for(p,n)  C1= "<<c1<<" C0= " <<c0<<endl;
		printall(arr, temp, i+1, k, n);
		//cout<<"\n Inside for(p,n)  C1= "<<c1<<" C0= " <<c0<<endl;

	}
	//cout<<"\n outside for(p,n) C1= "<<c1<<" C0= " <<c0<<endl;
}
}
void solve(char arr[], int n, int k) {

	char temp[k];
	printall(arr, temp, 0, k, n);
}
bool prime( long long int n1)
{
    long   int a;
    if(n1==337)
        cout<<"\n 337 reached should be prime " <<n1<<endl;
     long long int sq=sqrt(n1);
    for(a=2;a<=sq;a++)
    {
        if(n1==337)
        cout <<"n1=337 a = "<<a<<endl;
        if(n1%a==0)
        {
            if(n1==337)
            cout <<"n1=337 a that divides 337 is = "<<a <<endl;
            ck=true;
            vec.push_back(a);
            break;
        }
    }
    if(ck==false)
    {
        if(n1==337)
        cout<<"\n 337 Is Prime, ck = false  " <<n1<<endl;
        s="";
        vec.clear();

    }
    return ck;
}
void printvec(std::string st,vector<long int> v)
{
   //cout<<" \n factors being printed ";
   long long  int len=v.size();
//   long long int h = atoi (st);
    long long int ii = std::stoull (st,&sz,10);
   long int q;

   // cout<<st<<"\t";
   fprintf(f1,"%lld ",ii);
  //  cout<<" \n factors being printed ";
    for( q=0;q<len;q++){
        fprintf(f1,"%ld ",v[q]);

        //cout<<v[q]<<" ";
    }
    //cout<<endl;
   fprintf(f1,"\n");
    s="";
    j++;
    vec.clear();

}


int main() {

    int m,t;
    char arr[] = {'1', '0'};
	int n = sizeof(arr)/sizeof(arr[0]);
	f = fopen("in3.txt", "r");
    f1 = fopen("out3.txt", "w");
   // std::ofstream out("out3.txt");
    fscanf(f, "%d",&t);
    fscanf(f, "%d%d",&m,&jj);

	//cin>>m>>jj;
	//cout<<"Case #"<<cas<<":"<<endl;
	  fprintf(f1,"Case #%d:\n",cas);
    solve(arr, n, m);

    //cout<<"\n \n \n C1= "<<c1<<" C0= " <<c0<<endl;

	return 0;
}
