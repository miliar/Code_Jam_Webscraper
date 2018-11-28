#include <cstdio>
#include <string>
#include <map>
using namespace std;
map <string,int> d,tmp;
map <string,int>::iterator it;
int tc,n,l,tcn,cnt,re,check,ips;
char s[44];
string a[44],b[44],cur[44];
int main(void){
	//freopen("A-small-attempt2.in","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&tc);
	while(tc--){
		scanf("%d %d",&n,&l);
		for(int i = 0 ; i < n ; i++ ){
			scanf("%s",s);
			a[i]=s;
		}
		for(int i = 0 ; i < n ; i++ ){
			scanf("%s",s);
			b[i]=s;
			d[b[i]]++;
		}
		ips=1;

		for(int i = 0; i < (1<<(l)) ; i++ ){
			cnt=0;
			for(int j = 1 ; j < (1<<(l) ); j=j<<1){
				if(j&i)
					cnt++;
			}
			for(int j=0; j<n; j++)
				cur[j]="";
			for(int j = 1 ,idx=0; j < (1<<(l)) ; j=j<<1,idx++){
				if( j&i){
					for(int k=0; k< n; k++){
						if(a[k][idx]=='0')
							cur[k]+='1';
						else
							cur[k]+='0';
					}
				}
				else{
					for(int k=0; k< n; k++){
						cur[k]+=a[k][idx];
					}
				}
			}
			
			tmp.clear();
			
			for(int j =0; j< n; j++){
				tmp[cur[j]]++;
			}
			check=0;
			for(it = d.begin(); it!= d.end(); it++){
				if( (*it).second != tmp[(*it).first] )
					check=1;
			}
			if(!check){
				if(ips)
					re=cnt;
				else re=min(re,cnt);
				ips=0;
			}
		}
		printf("Case #%d: ",++tcn);
		if(ips)
			puts("NOT POSSIBLE");
		else printf("%d\n",re);
		d.clear();
		tmp.clear();
		for(int i=0; i<44; i++)
			cur[i]="";
	}
	return 0;
}