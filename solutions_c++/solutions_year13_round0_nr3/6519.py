#include<cstdio>
#include<cstdlib>
#include<cmath>

using namespace std;


int t,a,b,top,ans,pal[1024];

bool palin(int l){
	int bil,len,len2; bool cek=1; char temp[32];

	bil=l;
	for(len=0;bil>0;len++){
		temp[len]=(bil%10)+'0';
		bil/=10;
	}
	len2=len/2;
	for(int ll=0;ll<len2;ll++){
		if(temp[ll]!=temp[len-1-ll]){cek=0;break;}
	}
	if(cek)pal[l]=1;
	else pal[l]=-1;

	return cek;
}
void fair(int l){
	if(l<=top && pal[l]!=-1){
		if(pal[l]==0)palin(l);
		if(pal[l]==1){
			ans++;
			fair(l*l);
		}
	}
}

int main(){
	scanf("%d",&t);
	for(int no=1;no<=t;no++){
		scanf("%d%d",&a,&b);

		ans=0; top=b; a=ceil(sqrt(a)); b=sqrt(b);
		if(a==1){ans++; a+=1;}

		for(int l=a;l<=b;l++){
			if(pal[l]!=-1){
				if(pal[l]==0)palin(l);
				if(pal[l]==1){
					fair(l*l);
				}
			}
		}

		if(no>1)printf("\n");
		printf("Case #%d: %d",no,ans);
	}
return 0;
}
