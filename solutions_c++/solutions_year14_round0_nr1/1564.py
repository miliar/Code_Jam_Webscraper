#include<stdio.h>
#include<string.h>

#define if if (
#define then )
#define do )
#define for for (
#define while while (
#define begin {
#define end }

int T;
int a[5][5];
int b[5][5];
int p[17];

int main()
begin
	scanf("%d",&T);
	int tcase=0;
	while T-- do begin
		++tcase;
		int i,j;
		int a1,a2;
		scanf("%d",&a1);
		for i=1;i<=4;i++ do begin
			for j=1;j<=4;j++ do begin
				scanf("%d",a[i]+j);
			end;
		end;
		scanf("%d",&a2);
		for i=1;i<=4;i++ do begin
			for j=1;j<=4;j++ do begin
				scanf("%d",b[i]+j);
			end;
		end;
		memset(p,0,sizeof(p));
		for i=1;i<=4;i++ do ++p[a[a1][i]];
		for i=1;i<=4;i++ do ++p[b[a2][i]];
		int cnt=0,ans=0;
		for i=1;i<=16;i++ do begin
			if p[i]==2 then begin
				ans=i;
				++cnt;
			end;
		end;
		printf("Case #%d: ",tcase);
		if cnt==1 then begin
			printf("%d\n",ans);
		end else if cnt==0 then begin
			puts("Volunteer cheated!");
		end else begin
			puts("Bad magician!");
		end;
	end;
end