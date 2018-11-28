#include <cstdio>
#include <vector>
#include <algorithm>
#define pb push_back
using namespace std;
const int NMax=1100;
int N,A[NMax],avr;
vector<int> tmp;
int DFS(vector<int> s) {
	printf("%d\n",s.size());
	int nn=s.size(),ret=100000000,cnt=0;
	for(int i=0;i<nn;i++)cnt+=s[i];
	if(!cnt) return 0;
	vector<int> tmq;
	//for(int i=0;i<nn;i++) tmq[i]=max(0,tmq[i]-1);
	//ret=min(ret,DFS(tmq)+1);
	int maxx=-1;
	for(int i=0;i<nn;i++) maxx=max(maxx,s[i]);
	if(maxx==1) return 1;
	ret=min(ret,maxx);
	tmq=s;
	for(int j=0;j<nn;j++) {
		if(tmq[j]==maxx) {
			tmq[j]-=maxx/2;
			break;
		}
	}
	int flag=0;
	for(int j=0;j<nn;j++) {
		if(tmq[j]==0) {
			tmq[j]+=maxx/2;
			flag=1;
			break;
		}
	}
	if(!flag) tmq.pb(maxx/2);
	ret=min(ret,DFS(tmq)+1);
	return ret;
}
int main()
{
	FILE *fin=fopen("input.txt","r"),*fout=fopen("output.txt","w");
	int T;
	//memset(F,-1,sizeof(F));
	fscanf(fin,"%d",&T);
	for(int I=1;I<=T;I++) {
		printf("%d\n",I);
		fscanf(fin,"%d",&N);
		tmp.clear();
		int ret=0,maxx=0;
		for(int i=1;i<=N;i++) fscanf(fin,"%d",A+i),tmp.pb(A[i]),maxx=max(maxx,A[i]);
		ret=100000000;
		for(int i=maxx;i>=1;i--) {
			int cnt=0;
			vector<int> tmq=tmp;
			while(1) {
				int flag=0;
				for(int j=0;j<tmp.size();j++) if(tmp[j]==0) tmp.erase(tmp.begin()+j);
				for(int j=0;j<tmp.size();j++) {
					if(tmp[j]>i) {
						int x=tmp[j];
						tmp[j]=i;
						tmp.pb(x-i);
						cnt++;
						flag=1;
					}
				}
				if(!flag) break;
			}
			int maxx1=0;
			for(int j=0;j<tmp.size();j++)
				maxx1=max(maxx1,tmp[j]);
			cnt+=maxx1;
			//if(cnt>ret) break;
			ret=min(ret,cnt);
			tmp=tmq;
		}
		fprintf(fout,"Case #%d: %d\n",I,ret);
	}
	fclose(fin);fclose(fout);
	return 0;
}
