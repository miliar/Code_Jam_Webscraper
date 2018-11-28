#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
#include <list>
#include <set>
#include <queue>
#include <cstdio>


using namespace std;
typedef long long ll;
typedef long double ld;

#define Sz(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)	
#define Fc(i,s) for (i=s.begin(); i!=s.end(); i++)
#define Out(i,a) cout<<"Case #"<<i<<": "<<a<<endl

template<typename T> T Sqr(T x) { return(x*x); }


int t,i, j, k, m, n, l;
double w[27];
int p[27],tot;

int tempP[27], tempTot;
double tempW[27];

void updateWeight(double w[27], int p[27], int tot){
	int i;
//	cout<<"\nweight update\n";
	F0(i,n){
		w[i] = (double(p[i]))/tot;
		//cout<<w[i]<<"\n";
	}
}

int checkWeight(double w[27]){
	int i;
	F0(i,n){
		if(w[i]>0.5){
			return 0;
		}
	}
	
	return 1;
}

int maxWeight(){
	int i,j;
	double max=0;
	F0(i,n){
		if(max < w[i]){
			max = w[i];
			j = i;
		}
	}
	return j;
}


int main(){

	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	
	int x,y;
	int flag = 0;
	char ch;
	
	
	cin>>t;
	F1(i,t){
		tot=0;
		cin>>n;
		F0(j,n){
			
			cin>>p[j];
			tot += p[j];
		}
		

		cout<<"Case #"<<i<<":";
		
		updateWeight(w, p,tot);
		
		while(tot != 0){
			cout<<" ";
			x = maxWeight();	
			p[x]--;
			tot--;
			ch = 'A' + x;
			cout<<ch;
			
			updateWeight(w, p, tot);
			
			int val;
			
			flag =0;
			if(tot != 0)
			F0(k,n){
				//cout<<"1\n";
				tempTot = tot;
				F0(l,n){
					tempW[l] = w[l];
				}
				
				F0(l,n){
					tempP[l] = p[l];
				}
				
				tempP[k]--;
				tempTot--;
				
				updateWeight(tempW,tempP, tempTot);

				if(checkWeight(tempW)){flag = 1;val = k;break;	}
				
			}
			
			if(flag){
				
				//cout<<"4\n";

				ch = 'A' + val;
				cout<<ch;
				tot--;
				
				F0(l,n){
					w[l] = tempW[l];
				}
				
				F0(l,n){
					p[l] = tempP[l];
				}
			}		
			
		}
		cout<<"\n";
	}
	
	
	return 0;
}