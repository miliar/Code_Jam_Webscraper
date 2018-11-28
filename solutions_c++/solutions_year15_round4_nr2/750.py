#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
int L[1000],R[1000],nl,nr,E[1000],ne;
struct node
{
	double r,c;
}a[1000];
bool myfunction (node i,node j) { return (i.c<j.c); }
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.txt","w",stdout);
	
	int t,n,IMPOSSIBLE;
	double v,x,pp,rr,qq,t1,t2,vv;
	cin >> t;
	for(int aa=0;aa<t;aa++)
	{
		IMPOSSIBLE=0;nl=0;nr=0;ne=0;
		cin >> n >> v >> x;
		for(int i=0;i<n;i++)
		{
			scanf("%lf %lf",&a[i].r,&a[i].c);
			a[i].c-=x;
			if(a[i].c < 0.0) L[nl++] = i;
			else if(a[i].c > 0.0) R[nr++]=i;
			else E[ne++]=i;
		}
		x=0.0;
		sort(a,a+n,myfunction);
		/*cout << "_______";
		for(int i=0;i<n;i++)
		{
			cout << a[i].c << " ";
		}
		cout << endl;*/
		if(nl==0 and ne==0) IMPOSSIBLE = 1;
		if(nr==0 and ne==0) IMPOSSIBLE = 1;
		
		pp=0.0,qq=1000000.0;
		while(qq-pp > 1.0e-6)
		{
			rr=(pp+qq)/2.0;
			t1=0.0;
			vv=v;
			for(int i=0;i<n;i++)
			{
				if(vv >= rr*a[i].r)
				{
					vv-=rr*a[i].r;
					t1+=rr*a[i].r*a[i].c;
				}
				else
				{
					t1+=vv*a[i].c;
					vv=0.0;
					break;
				}
			}
			t2=0.0;
			vv=v;
			for(int i=n-1;i>=0;i--)
			{
				if(vv >= rr*a[i].r)
				{
					vv-=rr*a[i].r;
					t2+=rr*a[i].r*a[i].c;
				}
				else
				{
					t2+=vv*a[i].c;
					vv=0.0;
					break;
				}
			}
			//cout << rr << " " << t1 << " " << x*v << " " << t2 << endl;
			if(vv > 0.0) pp=rr;
			else if(t1<=x*v and x*v <=t2) 
			{
				//yes
				//cout << rr << " " << t1 << " " << x*v << " " << t2 << endl;
				qq=rr;
			}
			else pp=rr;
			
		}
			
		cout << "Case #" << aa+1 <<": ";
		if(IMPOSSIBLE == 1) cout << "IMPOSSIBLE" << endl;
		//else cout << pp << endl; 
		else printf("%.6lf\n",pp);
		
		
	}
}