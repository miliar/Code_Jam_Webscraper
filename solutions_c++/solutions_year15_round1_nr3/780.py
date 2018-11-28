/*********************************
ˮƽ����͹��   �����ϸ�Ͳ��ϸ�͹��
**********************************/
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<iostream>
#define op operator
#define db double
#define cp const Point&
#define rt return
#define cn const
using namespace std;
const double eps=1e-8;
inline int sig(double x)
{return (x>eps)-(x<-eps);}

struct Point
{
	db x , y;
	Point(db a = 0 , db b = 0):x(a),y(b){}
	bool   op < (cp b)const{
	    if(sig(x-b.x)!=0) rt sig(x-b.x) <0;
        rt sig(y-b.y) <0;}
    bool   op == (cp b)const{

        rt  sig(x-b.x) ==0 && sig(y-b.y) ==0;}

	Point  op + (cp a)const{rt Point(x+a.x ,y+a.y);}
	Point  op - (cp a)const{rt Point(x-a.x ,y-a.y);}
	db  op ^ (cp a)const{rt x*a.y - a.x * y;}
	db  op * (cp a)const{rt x*a.x + y*a.y;}
	Point  op * (cn db &a)const{rt Point(x*a,y*a);}
	bool op / (cp a)const{rt sig(x*a.y - a.x * y)==0;}
	db dis2(){rt fabs(x*x+y*y);}
	db dis() {rt sqrt(dis2());}
	db dis2(Point a){ rt fabs((x-a.x)*(x-a.x)+(y-a.y)*(y-a.y));}
	db dis(Point a) {rt sqrt(dis2(a));}
	Point T(){rt Point(-y,x);}
	void in(){scanf("%lf%lf",&x,&y);}
	void out(){printf("%lf %lf^^\n",x,y);}
	Point roate(double d)
	{ Point a;
	  a.x=x*cos(d)-y*sin(d);
	  a.y=y*cos(d)+x*sin(d);
	  return a;
    }
      //�жϵ��Ƿ���ƽ���߶��� a,bΪ�߶ζ˵�
    bool on(Point a,Point b){
        Point v1=a-*this,v2=b-*this;
        rt !sig(v1^v2) && sig(v1*v2)<=0;
    }
       //�ж��߶��ཻ
    bool seg(Point a1,Point b1,Point a2,Point b2){
        if(!sig((b1-a1)^(b2-a2)))
            rt a1.on(a2,b2) || a2.on(a1,b1) || b1.on(a2,b2) || b2.on(a1,b1);
        rt sig(((b1-a1)^(b2-a1)) * ((b1-a1)^(a2-a1))) <0 &&
           sig(((b2-a2)^(b1-a2)) * ((b2-a2)^(a1-a2))) <0;
    }
};

#define N  3100
/*
��͹��  ����㼯 �͵���
���� ͹���������
���ѿ��Ƕ��붥��֮�乲�ߵĵ�
*/
Point p[N];   //�������ݱ���������
/*
���ض���ξͱ���������  ����ʱ�뷽��
�����һ�������һ��Ԫ�� ��ͬһ����  ��֤�γɱջ�
���Ϊ�˽�Լ�ڴ�  ���԰�����s[]��Ϊ����p[]�ı��
*/
Point s[N];

inline int Graham(Point *s,int n)
{
	sort(p,p+n);
	s[0]=p[0];
    s[1]=p[1];

    int t=1;
	for(int i=2;i<n;i++){   //Ҫ�����ϵõ� ֻ��ȥ�� =
			while( t>0 && sig( (s[t]-s[t-1])^(p[i]-s[t-1]) )<0) t--;
			 s[++t]=p[i];
	  }
	int k=t;
	for(int i=n-2;i>=0;i--){  //Ҫ�����ϵõ� ֻ��ȥ�� =
			while( t>k && sig( (s[t]-s[t-1])^(p[i]-s[t-1]) )<0)t--;
			 s[++t]=p[i];
	  }
	  t++;
	  return t ;
}


Point q[N];

int main()
{
     freopen("C-small-attempt0.in","r",stdin);
    freopen("c.out","w",stdout);

    int T;
    scanf("%d",&T);

    for(int ca=1;ca<=T;ca++)
    {
         int n;
         scanf("%d",&n);
         for(int i=0;i<n;i++)  q[i].in();

          printf("Case #%d:\n",ca);

          if(n<4)
          {
               for(int i=0;i<n;i++) puts("0");
          }
          else{

            for(int i=0;i<n;i++)
            {

               int ans=3;

                for(int j=1;j < (1<<n);j++)
                {
                    int cnt =0;
                    p[cnt++]=q[i];
                    for(int k=0;k<n;k++)
                        if(j&(1<<k))
                    {
                        if(k!=i) p[cnt++]=q[k];
                    }

                    if(cnt <= ans) continue;
                    else {
                        int m= Graham(s,cnt);
                        for(int t=0;t<m;t++)
                            if(s[t]==q[i])
                        {
                            ans = cnt;
                        }
                    }

                }

                printf("%d\n",n-ans);
            }

          }
    }
    return 0;
}

















