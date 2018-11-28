#include <fstream>
#include <bits/stdc++.h>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
#define T pair<long long ,long long>
#define x first
#define y second
#define err pow(10,-8)
long long t,te,i,j,k,p,n;
ifstream f1;
FILE *f2;	
void lose(){
	cout<<"Case #"<<(te+1)<<": IMPOSSIBLE\n";
	fprintf(f2,"Case #%d: IMPOSSIBLE\n",te+1);
}
int main(){
	f1.open("input.txt");
	f2=fopen("output.txt","w");
	double r1,r2,c1,c2,v,x,ans,v1,v2,x1,x2;
	f1>>t;
	for(te=0;te<t;te++){
		f1>>n>>v>>x;
		if(n==1){
			f1>>r1>>c1;
			if(abs(x-c1)>err){
				lose();
				continue;		
			}
			ans=(v/r1);
		}
		else{
			f1>>r1>>c1>>r2>>c2;
			if((x>(c1+err)&&x>(c2+err))||((x<(c1-err)&&x<(c2-err)))){
				lose();
				continue;
			}
			if(abs(c1-c2)<err){
				ans=(v/(r1+r2));
			}
			else{
				if(abs(c2-x)<abs(c1-x)){
					swap(r1,r2);
					swap(c1,c2);
				}
				v1=(v*(x-c2))/(c1-c2);
				v2=v-v1;
				ans=max(v1/r1,v2/r2);
			}
		}
		cout<<"Case #"<<(te+1)<<": ";
		printf("%.9lf\n",ans);
		fprintf(f2,"Case #%d: %.9lf\n",te+1,ans);
	}
	f1.close();
	fclose(f2);
	return 0;
}
