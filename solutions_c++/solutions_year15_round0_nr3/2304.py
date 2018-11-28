#include<cstdio>
#include<cstring>
#include<vector>
#include<unordered_map>
using namespace std;

char str[10001];
vector<int> iflag;
vector<int> kflag;  // reverse
vector<int> DP;

int main(){
    unordered_map<int, unordered_map<int, int> > mularr;
    mularr[1][1] = 1;
    mularr[1]['i'] = 'i';
    mularr[1]['j'] = 'j';
    mularr[1]['k'] = 'k';
    mularr['i'][1] = 'i';
    mularr['i']['i'] = -1;
    mularr['i']['j'] = 'k';
    mularr['i']['k'] = 0-'j';
    mularr['j'][1] = 'j';
    mularr['j']['i'] = 0-'k';
    mularr['j']['j'] = -1;
    mularr['j']['k'] = 'i';
    mularr['k'][1] = 'k';
    mularr['k']['i'] = 'j';
    mularr['k']['j'] = 0-'i';
    mularr['k']['k'] = -1;

    int T, L, X;
    scanf(" %d ", &T);
    for(int t=1; t<=T; ++t){
	DP.clear();
	iflag.clear();
	kflag.clear();

	scanf(" %d %d ", &L, &X);
	scanf("%s", str);
	for(int i=1; i<X; ++i)	strncat(str, str, L);
	int len = L*X;

	int cur = 1;
	for(int i=0; i<len; ++i){
	    if(cur > 0)	cur = mularr[cur][str[i]];
	    else    cur = 0-(mularr[0-cur][str[i]]);
	    if(cur == 'i')  iflag.push_back(i);
	    //iflag[i] = (cur == 'i');
	}
	cur = 1;
	for(int i=len-1; i>=0; --i){
	    if(cur > 0)	cur = mularr[str[i]][cur];
	    else    cur = 0-(mularr[str[i]][0-cur]);
	    if(cur == 'k'){
		kflag.push_back(i);
		DP.push_back(-2);
	    }
	    //kflag[i] = (cur == 'k');
	}

	if(iflag.size() == 0 || kflag.size() == 0){
	    printf("Case #%d: NO\n", t);
	    continue;
	}

	bool res = false;
	for(int i=iflag.size()-1; i>=0; --i){
	    int k=kflag.size()-1;
	    while(k >= 0 && kflag[k] <= iflag[i]) --k;
	    if(k < 0)	continue;

	    if(i==iflag.size()-1 || kflag[k]<=iflag[i+1]){
		cur = 1;
		int j=iflag[i]+1;
		while(k>=0 && (i==iflag.size()-1 || kflag[k]<=iflag[i+1])){
		    for(; j<kflag[k]; ++j){
			if(cur > 0)	cur = mularr[cur][str[j]];
			else    cur = 0-(mularr[0-cur][str[j]]);
		    }
		    DP[k] = cur;
		    if(DP[k] == 'j'){
			res = true;
			break;
		    }
		    --k;
		}
		if(k < 0)   continue;
		for(; j<=iflag[i+1]; ++j){
		    if(cur > 0)	cur = mularr[cur][str[j]];
		    else    cur = 0-(mularr[0-cur][str[j]]);
		}
		while(k >= 0){
		    DP[k] = mularr[cur][DP[k]];
		    if(DP[k] == 'j'){
			res = true;
			break;
		    }
		    --k;
		}
	    }else{
		cur = 1;
		for(int j=iflag[i]+1; j<=iflag[i+1]; ++j){
		    if(cur > 0)	cur = mularr[cur][str[j]];
		    else    cur = 0-(mularr[0-cur][str[j]]);
		}
		while(k >= 0){
		    DP[k] = mularr[cur][DP[k]];
		    if(DP[k] == 'j'){
			res = true;
			break;
		    }
		    --k;
		}
	    }
	    if(res) break;
	}
	if(res)	printf("Case #%d: YES\n", t);
	else	printf("Case #%d: NO\n", t);
    }
    return 0;
}
