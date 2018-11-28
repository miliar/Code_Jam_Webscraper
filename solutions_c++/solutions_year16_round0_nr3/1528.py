#include<cstdio>
#include<algorithm>
#include<set>
#include<string>
#include<cassert>
using namespace std;
void printdiv(){
  printf("3 2 3 2 7 2 3 2 3\n");
}
set<string>dict;
set<string>global;
int n,m;

void verify(string a){
  assert(global.find(a)==global.end());
  assert((int)a.size()==n);
  int par=0,impar=0;
  for(int i=0;i<n;i++){
    assert(a[i]=='0' || a[i]=='1');
    if(i&1)impar+=a[i]-'0';
    else par+=a[i]-'0';
  }
  //  if(par!=impar)printf("%s\n",a.c_str());
  assert(par==impar);
  assert(((par+impar)%2)==0);
}
int main(){
  int tt;
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++){
    global.clear();
    dict.clear();
    scanf("%d %d",&n,&m);
    int foi=0;
    string a="";
    printf("Case #%d:\n",rr);
    for(int i=0;i<((n-2)/2);i++){
      a += "0";
    }
    int x=((n-2)/4);
    while(x%3!=2)x+=1;
    for(int i=0;i<x;i++){
      a[i]='1';
    }
    while(true){
      while(dict.find(a)!=dict.end()){
	random_shuffle(a.begin(),a.end());
	//	printf("%s\n",.str());
      }
      dict.insert(a);
      set<string> dict2;
      string b = a;
      

      while(foi<m){
	string end="";
	end.push_back('1');
	for(int i=0;i<(int)a.size();i++){
	  end.push_back(a[i]);
	  end.push_back(b[i]);
	}
	end.push_back('1');
	verify(end);
	global.insert(end);
	dict2.insert(b);
	printf("%s ",end.c_str());
	printdiv();
	foi++;
	int kkk=0;
	while(true){
	  random_shuffle(b.begin(),b.end());
	  kkk++;
	  if(kkk==m)break;
	  if(dict2.find(b)==dict2.end())break;
	}
	if(kkk==m)break;
      }
      if(foi==m)break;
    }

  }
  return 0;
}
