#include<bits/stdc++.h>
using namespace std;

typedef pair<double,double> pdd;

int n;
double v,x;
double deb,temp,tempe;

pdd s[100];//temp,debit

void recomp(int a, int b)
{
  deb=0;temp=0;tempe=0;
  for(int i=a;i<b;i++)
    {
      deb+=s[i].second;
      temp+=s[i].first*s[i].second;
    }
  tempe=temp/deb;
  return;
}

int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d: ",cas);
	// solution
	scanf("%d%lf%lf",&n,&v,&x);
	for(int i=0;i<n;i++)
	  scanf("%lf%lf",&s[i].second,&s[i].first);
	//calculer débit total, température totale.
	recomp(0,n);
	//done
	sort(s,s+n);
	if(cas==-1){
	  printf("%d\n",n);
	  printf("%lf %lf\n",x,v);
	  for(int i=0;i<n;i++)
	    printf("%lf %lf\n",s[i].first,s[i].second);
	}
	
	if(s[0].first-1E-12>x || s[n-1].first +1E-12<x)
	  {
	    printf("IMPOSSIBLE\n");
	    continue;
	  }
	if(tempe+1E-12<x)//froid
	  {
	    if(cas==-1) cerr << "too cold" << tempe << endl;
	    for(int i=0;i<n-1;i++)
	      {
		if(abs(tempe-x)<1E-8)break;
		if(cas==-1)cerr << "remove " << i << s[i].first << "temp" << tempe << "x" << x << "dif" << abs(tempe-x)<< endl;
		recomp(i+1,n);
		if(tempe-1E-12>x)//too much
		  {
		    if(cas==-1)cerr << "too much " << i << tempe << endl;
		    double ri = (temp - x*deb)/(x-s[i].first);
		    if(cas==-1)printf("%lf\n",ri);
		    temp += ri*s[i].first;
		    deb+=ri;
		    if(cas==-1)printf("tempe %lf x %lf\n",temp/deb,x);
		    break;
		  }
	      }
	  }
	else if(tempe-1E-12>x)//hot
	  {
	    if(cas==-1)cerr << "too hott" << endl;
	    for(int i=n-1;i>0;i--)
	      {
		if(abs(tempe-x)<1E-12)break;
		recomp(0,i);
		if(tempe+1E-12<x)//too much
		  {
		    double ri = (temp- x*deb)/(x-s[i].first);
		    temp+=ri*s[i].first;
		    deb+=ri;
		    break;
		  }
	      }
	  }
	printf("%.10lf\n",v/deb);
	// end
    }
    return 0;
}
