#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<iostream>
#include<queue>
#include<stack>
#include<math.h>

using namespace std;

FILE *fin;
FILE *fout;

int n,x;
int a[10010];

int solve(){
	int ans = 0;
	map<int,int> myset;
	for(int i = 1;i <= n;++i){
		if(myset.find(-a[i]) == myset.end())
			myset[-a[i]] = 0;
		++myset[-a[i]];
	}
	while(myset.size() > 0){
		++ans;
		map<int,int>::iterator it = myset.begin();
//		--it;
		int now = it->first;
		now = -now;
		if(it->second == 1)
			myset.erase(it);
		else
			--myset[it->first];
	//	printf("now: %d\n",now);
		if(myset.size() == 0)
			break;
		it = myset.lower_bound(now - x);
		if(it != myset.end()){
		//	printf("found %d\n",it->first);
			if(it->second == 1)
				myset.erase(it);
			else
				--myset[it->first];
		}
	}
	return ans;
}

bool deleted[10010];
int brute_solve(){
	int ans = 0;
	sort(a + 1,a + 1 + n);
	int remain = n;
	int p = 1;
	memset(deleted,false,sizeof(deleted));
	while(remain > 0){
		++ans;
		deleted[p] = true;
		--remain;
		for(int i = n;i >= 1;--i){
			if(deleted[i] == false && a[p] + a[i] <= x){
				deleted[i] = true;
				--remain;
				break;	
			}	
		}
		while(deleted[p] == true)
			++p;
	}
	return ans;		
}

int main(){
	fin = fopen("A-large.in","r");
	fout = fopen("ans.txt","w");
	int T;
	fscanf(fin,"%d",&T);
	for(int cas = 1;cas <= T;++cas){
		fscanf(fin,"%d%d",&n,&x);
		for(int i = 1;i <= n;++i)
			fscanf(fin,"%d",&a[i]);
		fprintf(fout,"Case #%d: %d\n",cas,solve());
//		printf("brute: %d\n",brute_solve());
//		printf("%d\n",solve());
	}
	fclose(fin);
	fclose(fout);
	system("pause");
	return 0;
}

