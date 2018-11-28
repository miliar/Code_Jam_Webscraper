#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;

int  main(){
	vector<double> N;
	vector<double> K;
	FILE * fp;
	FILE * fpo;
	fp = freopen("D-large.in","r",stdin);
//	fp = freopen("inputCJ4.txt","r",stdin);
	fpo = freopen("outputCJ41.txt","w",stdout);
	N.clear();
	K.clear();
	double d;
	int t,n,i,j;
	int fair = 0,unfair = 0;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		fair = 0;
		unfair = 0;
		N.clear();
		K.clear();
		scanf("%d",&n);
		for(j=0;j<n;j++){
			//scanf("%lf",&d);
			cin >> d;
			N.push_back(d);
		}
		for(j=0;j<n;j++){
			scanf("%lf",&d);
			K.push_back(d);
		}
		
		sort(N.begin(),N.end());
		sort(K.begin(),K.end());
		
		//get unfair score
		double minK = K.at(0);
		double maxK = K.at(n-1);
		j=0;
		for(int z = 0 ; z < n ; z++){
			if(N.at(z) < maxK){
				if (N.at(z) > K.at(j)){
					unfair+=1;
					j+=1;
				}
			}
			else
				unfair+=1;
		}
		
		//get fair score
		j=0;
		int k =0;
		while(k < n){
			if (N.at(j) < K.at(k))
				j++;
			k++;
		}
		fair = n-j;
		cout << "Case #" << i << ": " << unfair << " " << fair << endl;
	}
}
