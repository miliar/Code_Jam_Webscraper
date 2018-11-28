#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
#define NULL 0
#define pp double
struct A
{
	int n;//最大农场数目
	pp C ,F,X;
	pp v;//生产速度
	pp t;//时间

	struct A *next;
};
int main()
{
	fstream f("B-small-attempt1.in",ios::in);
	int n;
	f>>n;
	int i,j,k;
	A *p,*h;

	pp v,kk;
	h=(A *)malloc(sizeof(struct A));
	p=h;
	p->next=NULL;
	for(i=0;i<n;i++)
	{
		f>>p->C>>p->F>>p->X;
		v=2.0f;
		for(j=0;;j++)
		{
			kk=((p->X-p->C)/v)-(p->X/(v+p->F));
			if(kk<0)
			{
				p->n=j;
				break;
			}
			v+=p->F;

		}
		p->next=(A *)malloc(sizeof(struct A));
		p=p->next;
		p->next=NULL;
	}
	f.close();
	fstream f1("B-small-attempt1.out",ios::out);
	//input OK;
	p=h;
	for(i=0;i<n;i++)
	{
		p->t=0.0;
		p->v=2.0;
		for(j=0;j<p->n;j++)
		{
			p->t+=p->C/p->v;
			p->v+=p->F;
		}
		p->t+=p->X/p->v;	
		p=p->next;
	}


	p=h;
	for(i=0;i<n;i++)
	{
		f1<<"Case #"<<fixed<<setprecision(7)<<(i+1)<<": "<<p->t<<endl;;
		p=p->next;
	}
	return 0;
}