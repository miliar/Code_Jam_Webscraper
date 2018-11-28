#include<bits/stdc++.h>

using namespace std;

int a[10];
typedef long long lg;

int main(){
	int test, val, p;
	lg n, ult, aux, k, resto;
	/*freopen("A-large.in", "r", stdin);
	ofstream file;
    file.open ("out_a.txt");*/
	
	scanf("%d", &test);
	for(int i=1; i<=test; i++){
		cin>>n;
		memset(a, 0, sizeof(a));
		p=0;
		k=1;
		while(p<10 && n!=0){
			aux=n*k;
			ult=aux;
			while(aux>0 && p<10){
				resto=aux%10;
				if(!a[resto]){
					a[resto]=1;
					p++;
				}
				aux/=10;
			}
			k++;
		}
		printf("Case #%d: ", i);
		if(p==10)	printf("%d\n", ult);
		else	printf("INSOMNIA\n");
		
		/*file<<"Case #"<<i<<": ";
		if(p==10)	file<<ult<<"\n";
		else	file<<"INSOMNIA\n";
		*/
	}
	//file.close();
	return 0;
}