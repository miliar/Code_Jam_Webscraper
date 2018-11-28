#include <bits/stdc++.h>

using namespace std;

#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define sz(x) ((int)(x).size())
#define all(c) (c).begin(),(c).end()
#define forn(i, n) for (int i = 0; i < (n); i++)
typedef long long ll;

int main(){
	int T, D, P;
	ll Min, Di1, Di2, Da, Mia, Ma;
	scanf("%d", &T);
	map<ll, ll> M, Aux, Au;
	map<ll, ll>::iterator it, ita;
	for(int lol=1; lol<=T; ++lol){
		scanf("%d", &D);
		M.clear();
		for(int i=0; i<D; ++i){
			scanf("%d", &P);
			M[P]++;
		}
		Min=100000;
		stack<pair<map<ll, ll>, ll > > S;
		S.push(make_pair(M, 0));
		while(!S.empty()){
			Aux=S.top().first;
			Mia=S.top().second; S.pop();
			it=Aux.end(); it--;
			int Top=it->first, TopC=it->second;
//			cout<<"M "<<Auxx<<"C "<<Mia<<endl;
			Min=min(Top + Mia, Min);
			if(Aux.size()==1){
				for(int i=2; i<=Top; ++i){
					Au=Aux;
					Di1=ceil((double)Top/(double)i);
      				Di2=floor((double)Top/(double)i);
					if(!Di2) break;
					if(Di1+(TopC*(i-1)) > Top) break;
					Ma=Mia+(TopC*(i-1));
					Da=(Top%i);
					//if ....
						Au.clear();
						Au[Di1]+=Da;
						Au[Di2]+=i-Da;
						S.push(make_pair(Au, Ma));
						//}else{
						//break;
						//}
				}
			}else{
				for(int i=2; i<=Top; i++){
					Au=Aux;
					it=Au.end(); it--;
					ita=it; ita--; 
	    			Di1=ceil((double)Top/(double)i);
		    		Di2=floor((double)Top/(double)i);
			    	//cout<<i<<":"<<Di1<<Di2<<ita->first<<endl;
    				//if(Di1 < ita->first)
					if(!Di2 ) break;
					if(max(Di1, ita->first)+(TopC*(i-1)) > Top ) break;
					Ma=Mia+(TopC*(i-1));
	    		    Da=(Top%i); //ceil
			    	Au.erase(it);
	    		   	Au[Di1]+=Da;
		    	   	Au[Di2]+=i-Da;
				    S.push(make_pair(Au, Ma)); 
			    }
			}
		}
		printf("Case #%d: %lld\n", lol, Min);
	}
    return 0;
}
