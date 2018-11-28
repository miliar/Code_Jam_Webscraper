#include<cstdio>
#include<algorithm>
#include<vector>

using namespace std;

int T;
int main(){
	scanf("%d", &T);
	for(int i=1; i<=T; i++){
	    int a1 = 0, a2 = 0, n, tmp, mm=0;
	    vector<int> mr;
	    scanf("%d", &n);
	    for(int j=0; j<n; j++){
		scanf("%d", &tmp);
		mr.push_back(tmp);
		if((mr.size()>1)&&mr[mr.size()-1] < mr[mr.size()-2]){
		    a1 += mr[mr.size()-2] - mr[mr.size()-1];
		    mm = max(mm, mr[mr.size()-2] - mr[mr.size()-1]);
		}
	    }
	    for(int j=0; j<n-1; j++){
		if(mr[j] <= mm){
		    a2 += mr[j];
		}
		else{
		    a2 += mm;
		    //mr[j+1] += mr[j] - mm;
		}
	    }
	    printf("Case #%d: %d %d\n", i, a1, a2);
	}
}
