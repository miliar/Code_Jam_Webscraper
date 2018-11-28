#include<vector>
#include<cstdio>
#include<algorithm>
#include<string>
#include<map>
#include<cstring>
using namespace std;
map<string, int> dict;
int lan[50000];
int old[50000];
char ent[99999];
vector<int> val[50];
int n;
int v;
int main () {
  int tt;
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++) {
    dict.clear();
    //    lan.clear();
    //    old.clear();
    memset(lan,0,sizeof(lan));
    v=1;
    scanf("%d ",&n);
    for(int i=0;i<n;i++){
      val[i].clear();
      gets(ent);
      int len = strlen(ent);
      ent[len]=' ';
      //      printf("%s\n",ent);
      string at = "";
      for(int j=0;j<=len;j++){
	if (ent[j]!=' '){
	  at.push_back(ent[j]);
	}
	else {

	  if (dict.find(at)==dict.end()){
	    dict[at] = v++;
	  }
	  int r = dict[at];
	  val[i].push_back(r);
	  
	  if (i==0)
	    {
	      lan[r] |= 1;
	    }
	  else if(i==1)
	    {
	      lan[r] |= 2;
	    }
	  //	   printf("%d %d\n",r,lan[r]);
	  at = "";
	}
      }
    }
    int ret = 0x3f3f3f3f;
    for(int i=0;i<(1<<(n-2));i++){
      //      old = lan;
      for(int j=0;j<=v;j++)
	old[j]=lan[j];
      for(int j=2;j<n;j++){
	int t = 1;
	if (i & (1<<(j-2)))t=2;
	//	printf("%d %d %d\n",i,j,t);
	for(int k=0;k<val[j].size();k++){
	  lan[val[j][k]]|=t;
	}
      }
      int at =0;
      for(int j=1;j<=v;j++){
	if(lan[j]==3)at++;
      }
      for(int j=0;j<=v;j++)
	lan[j]=old[j];
     
      ret = min(ret,at);
    }
    printf("Case #%d: %d\n",rr,ret);
    //    for( int i=0;
  }
  return 0;
}
