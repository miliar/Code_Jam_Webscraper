#include<stdio.h>
int tcn,tc;
int p;
char input[210][20000];
int ilen[210];
int wn[210];
int wlen[210][1010];
char wlist[210][1010][20];
int wd[210][1010];
int dwl[5000];
char dict[5000][20];
int dlen;
int ans;
int n,m;
int edge[100000][3];
int en[5000];
int elist[200000][3];
int chk[5000];
int qs,qe;
int q[5000];
int bedge[5000][2];
void addedge(int x,int y,int g){
	edge[m][0]=x;
	edge[m][1]=y;
	edge[m][2]=g;
	m++;
}
int main(){
	int i,j,k,l;
	FILE *in=fopen("input.txt","r");
	freopen("output.txt","w",stdout);
	fscanf(in,"%d",&tcn);
	for(tc=1;tc<=tcn;tc++){
		fscanf(in,"%d",&p);
		for(i=0;i<p;i++){
			fgets(input[i],18000,in);
			for(ilen[i]=0;input[i][ilen[i]];ilen[i]++);
			wn[i]=0;
			for(j=0;j<ilen[i];){
				if(input[i][j]>='a'&&input[i][j]<='z'){
					for(k=j;input[i][k]>='a'&&input[i][k]<='z';k++){
						wlist[i][wn[i]][k-j]=input[i][k];
					}
					wlen[i][wn[i]]=k-j;
					wn[i]++;
					j=k;
				}
				else j++;
			}
			if(wn[i]==0)i--;
		}
		dlen=0;
		ans=0;
		for(i=0;i<p;i++){
			for(j=0;j<wn[i];j++){
				for(k=0;k<dlen;k++){
					if(wlen[i][j]!=dwl[k])continue;
					for(l=0;l<dwl[k];l++){
						if(dict[k][l]!=wlist[i][j][l]){
							break;
						}
					}
					if(l==dwl[k]){
						wd[i][j]=k;
						break;
					}
				}
				if(k==dlen){
					wd[i][j]=dlen;
					dwl[dlen]=wlen[i][j];
					for(l=0;l<wlen[i][j];l++){
						dict[dlen][l]=wlist[i][j][l];
					}
					dlen++;
				}
			}
		}
		n=2*dlen+2;
		m=0;
		for(i=0;i<dlen;i++){
			addedge(i,i+dlen,1);
		}
		for(i=0;i<wn[0];i++){
			addedge(dlen*2,wd[0][i],1000000);
		}
		for(i=0;i<wn[1];i++){
			addedge(wd[1][i]+dlen,dlen*2+1,1000000);
		}
		for(i=2;i<p;i++){
			for(j=0;j<wn[i];j++){
				for(k=0;k<wn[i];k++){
					if(j==k)continue;
					addedge(wd[i][j]+dlen,wd[i][k],1000000);
				}
			}
		}
		for(i=0;i<n+3;i++){
			en[i]=0;
		}
		for(i=0;i<m;i++){
			en[edge[i][0]+2]++;
			en[edge[i][1]+2]++;
		}
		for(i=0;i<n+3;i++){
			en[i+1]+=en[i];
		}
		for(i=0;i<m;i++){
			elist[en[edge[i][0]+1]][0]=edge[i][1];
			elist[en[edge[i][0]+1]][1]=edge[i][2];
			elist[en[edge[i][0]+1]][2]=en[edge[i][1]+1];
			elist[en[edge[i][1]+1]][0]=edge[i][0];
			elist[en[edge[i][1]+1]][1]=0;
			elist[en[edge[i][1]+1]][2]=en[edge[i][0]+1];
			en[edge[i][0]+1]++;
			en[edge[i][1]+1]++;
		}
/*		for(i=0;i<dlen;i++){
			printf("%s\n",dict[i]);
		}
		for(i=0;i<n;i++){
			printf("%d %d\n",i,en[i+1]-en[i]);
			for(j=en[i];j<en[i+1];j++){
				printf("%d %d %d\n",elist[j][0],elist[j][1],elist[j][2]);
			}
		}*/
		while(1){
			for(i=0;i<n;i++){
				chk[i]=0;
			}
			qs=0;
			qe=1;
			q[0]=n-2;
			chk[n-2]=1;
			while(qs<qe){
				for(i=en[q[qs]];i<en[q[qs]+1];i++){
					if(elist[i][1]>0&&chk[elist[i][0]]==0){
						bedge[elist[i][0]][0]=q[qs];
						bedge[elist[i][0]][1]=i;
						chk[elist[i][0]]=1;
						q[qe]=elist[i][0];
						qe++;
					}
				}
				qs++;
			}
			if(chk[n-1]==0){
				break;
			}
			ans++;
			i=n-1;
			while(i!=n-2){
				elist[bedge[i][1]][1]--;
				elist[elist[bedge[i][1]][2]][1]++;
				i=bedge[i][0];
			}
		}
		printf("Case #%d: %d\n",tc,ans);
	}
}