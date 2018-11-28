#include<iostream>
#include<fstream>
#include<string>
using namespace std;
#define NULL 0
struct A
{
	int n;//输入的序号
	int a[4];
	int b[17],b1[4];
	int c[17],c1[4];
	struct A *next;

};
int main()
{
	fstream f("A-small-attempt1.in",ios::in);
	int n;//输入的个数
	int i,j,k;//无关
	f>>n;
	A *h,*p;//h头指针不变
	h=(A *)malloc(sizeof(struct A));
	p=h;
	p->next=NULL;
	
	for(i=0;i<n;i++)
	{
		f>>p->b[0];
		for(j=0;j<4;j++)
		{
			f>>p->b[1+4*j]>>p->b[2+4*j]>>p->b[3+4*j]>>p->b[4+4*j];
			if(j+1==p->b[0])
			{
				p->b1[0]=p->b[1+4*j];
				p->b1[1]=p->b[2+4*j];
				p->b1[2]=p->b[3+4*j];
				p->b1[3]=p->b[4+4*j];
			}
		}
		f>>p->c[0];
		for(j=0;j<4;j++)
		{
			f>>p->c[1+4*j]>>p->c[2+4*j]>>p->c[3+4*j]>>p->c[4+4*j];
			if(j+1==p->c[0])
			{
				p->c1[0]=p->c[1+4*j];
				p->c1[1]=p->c[2+4*j];
				p->c1[2]=p->c[3+4*j];
				p->c1[3]=p->c[4+4*j];
			}
		}
		p->next=(A *)malloc(sizeof(struct A));
		p=p->next;
		p->next=NULL;		
	}
//input OK


//执行

	p=h;
	for(i=0;i<n;i++)
	{
		p->n=0;
		for (j=0;j<4;j++)
		{
			p->a[j]=-1;
			for(k=0;k<4;k++)
			{
				if(p->b1[j]==p->c1[k])
				{
					p->a[j]=p->b1[j];
					p->n+=1;
					break;
				}
			}
		}
		p=p->next;
	}
	f.close;
//Output
	fstream f1("A-small-attempt1.out",ios::out);
	p=h;
	for(i=0;i<n;i++)
	{
		if(p->n==1)
		{
			for(j=0;j<4;j++)
			{
				if(p->a[j]!=-1)
				{
					f1<<"Case #"<<(i+1)<<": "<<p->a[j]<<endl;
					break;
				}
			}
		}
		else{ 
			if(p->n>1)
			{
				f1<<"Case #"<<(i+1)<<": Bad magician!"<<endl;
			}
			else
			{
				if(p->n==0)
				{
					f1<<"Case #"<<(i+1)<<": Volunteer cheated!"<<endl;
				}
			}
	
		}
		p=p->next;
	}
	f1.close;
//检测
	/**
	p=h;
	for(i=0;i<n;i++)
	{
		cout<<p->b[0]<<endl;
		for(j=0;j<4;j++)
		{
			cout<<p->b[1+4*j]<<" "<<p->b[2+4*j]<<" "<<p->b[3+4*j]<<" "<<p->b[4+4*j]<<" "<<endl;
		}
		cout<<p->c[0]<<endl;
		for(j=0;j<4;j++)
		{
			cout<<p->c[1+4*j]<<" "<<p->c[2+4*j]<<" "<<p->c[3+4*j]<<" "<<p->c[4+4*j]<<" "<<endl;
		}
		
			cout<<p->b1[0]<<" "<<p->b1[1]<<" "<<p->b1[2]<<" "<<p->b1[3]<<" "<<endl;
			cout<<p->c1[0]<<" "<<p->c1[1]<<" "<<p->c1[2]<<" "<<p->c1[3]<<" "<<endl;
		
	}
**/
	return 0;
}