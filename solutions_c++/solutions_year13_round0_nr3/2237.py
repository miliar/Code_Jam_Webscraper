#include<iostream>
#include<fstream>
#include<sstream>
using namespace std;
ifstream fin("c.in");
ofstream fout("c.out");
stringstream ss;
int tot;
long long list[100001];
int check(long long num){
  int l,i;
  string str;
  ss.clear();
  ss<<num;
  ss>>str;
  l=str.length();
  for(i=0;i<=l>>1;i++)
	if(str[i]!=str[l-i-1])return(0);
  return(1);
}
void generate(int num){
  int i,k,l;
  long long temp;
  char ch;
  string str,reverse,mid,s1;
  ss.clear();
  ss<<num;
  ss>>str;
  reverse=str;
  l=str.length();
  for(i=0;i<=l-1;i++)
	reverse[i]=str[l-i-1];
  s1=str+reverse;
  ss.clear();
  ss<<s1;
  ss>>k;
  temp=k;
  temp*=k;
  if(check(temp)){
	tot++;
	list[tot]=temp;
  }
  mid=" ";
  for(ch='0';ch<='9';ch++){
	mid[0]=ch;
	s1=str+mid+reverse;
	ss.clear();
	ss<<s1;
	ss>>k;
	temp=k;
	temp*=k;
	if(check(temp)){
	  tot++;
	  list[tot]=temp;
	}
  }
}
void qs(int l,int r){
  int i,j;
  long long x;
  i=l;j=r;x=list[(l+r)>>1];
  while(i<=j){
	while(list[i]<x)i++;
	while(list[j]>x)j--;
	if(i<=j){
	  swap(list[i],list[j]);
	  i++;j--;
	}
  }
  if(i<r)qs(i,r);
  if(l<j)qs(l,j);
}
void init(){
  int i;
  tot=3;
  list[1]=1;list[2]=4;list[3]=9;
  for(i=1;i<=1000;i++)
	generate(i);
  qs(1,tot);
  /*for(i=1;i<=tot;i++)
	fout<<list[i]<<endl;*/
}
void solve(){
  int i,j,n,ans;
  long long a,b;
  fin>>n;
  for(i=1;i<=n;i++){
	fin>>a>>b;
	ans=0;
	for(j=1;j<=tot;j++)
	  if(list[j]>=a&&list[j]<=b)ans++;
	fout<<"Case #"<<i<<": "<<ans<<endl;
  }
}
int main(){
  init();
  solve();
  return(0);
}
