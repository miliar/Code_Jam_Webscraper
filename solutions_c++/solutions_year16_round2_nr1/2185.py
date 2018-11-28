#include<cstdio>
#include<cstring>
char s[2010];
int cnt[26],c[10];
int main(){
    freopen("A-large.bin","r",stdin);
    freopen("output","w",stdout);
	int t;scanf("%d",&t);
        int i,j;
	for(int cas=1;cas<=t;cas++){
		scanf("%s",s);
                for(i=0;i<26;i++)cnt[i]=0;
                for(i=0;i<10;i++)c[i]=0;
		for(i=0;s[i];i++)cnt[s[i]-'A']++;
                c[0]=cnt[25];
                cnt[4]-=cnt[25],cnt[17]-=cnt[25],cnt[14]-=cnt[25];
                c[2]=cnt[22];
                cnt[19]-=cnt[22],cnt[14]-=cnt[22];
                c[6]=cnt[23];
                cnt[18]-=cnt[23],cnt[8]-=cnt[23];
                c[7]=cnt[18];
                cnt[4]-=cnt[18]*2,cnt[21]-=cnt[18],cnt[13]-=cnt[18];
                c[8]=cnt[6];
                cnt[4]-=cnt[6],cnt[8]-=cnt[6],cnt[7]-=cnt[6],cnt[19]-=cnt[6];
                c[3]=cnt[19];
                cnt[4]-=cnt[19]*2,cnt[7]-=cnt[19],cnt[17]-=cnt[19];
                c[4]=cnt[17];
                cnt[5]-=cnt[17],cnt[14]-=cnt[17],cnt[20]-=cnt[17];
                c[5]=cnt[5];
                cnt[8]-=cnt[5],cnt[21]-=cnt[5],cnt[4]-=cnt[5];
                c[1]=cnt[14];
                c[9]=cnt[8];
                printf("Case #%d: ",cas);
                for(i=0;i<10;i++)for(j=0;j<c[i];j++)printf("%d",i);
                printf("\n");
	}
	return 0;
}
