#include<stdio.h>
#include<algorithm>

#define if if (
#define then )
#define do )
#define for for (
#define while while (
#define begin {
#define end }

int T;
int n;
double a[1005];
double b[1005];

inline void solve1()
begin
	int ans=0;
	std::sort(a+1,a+n+1);
	std::sort(b+1,b+n+1);
	int l2=1,r2=n;
	int i;
	for i=1;i<=n;i++ do begin
		if a[i]<b[l2] then begin
			--r2;
		end else begin
			++l2;
			++ans;
		end;
	end;
	printf("%d ",ans);
end;

inline void solve2()
begin
	int ans=0;
	int i;
	int l2=1;
	for i=1;i<=n;i++ do begin
		while l2<=n && a[i]>b[l2] do ++l2;
		if l2>n then break;
		++l2;
	end;
	ans=n-i+1;
	printf("%d\n",ans);
end;

inline void solve()
begin
	solve1();
	solve2();
end;

int main()
begin
	scanf("%d",&T);
	int tno=0;
	while T-- do begin
		++tno;
		scanf("%d",&n);
		int i;
		for i=1;i<=n;i++ do begin
			scanf("%lf",a+i);
		end;
		for i=1;i<=n;i++ do begin
			scanf("%lf",b+i);
		end;
		printf("Case #%d: ",tno);
		solve();
	end;
end