#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <math.h>
#include <string.h>
using namespace std;

/**
 * ��άACM���㼸��ģ��
 * ע��������͸��ĺ�EPS
 * #include <cmath>
 * #include <cstdio>
 * By OWenT
 */
const int N=5e4+9;
const double eps = 1e-8;
const double pi = acos(-1.0);
//��
class point
{
public:
    double x, y;
    point(){};
    point(double x, double y):x(x),y(y){};

    static int xmult(const point &ps, const point &pe, const point &po)
    {
        return (ps.x - po.x) * (pe.y - po.y) - (pe.x - po.x) * (ps.y - po.y);
    }

    //���ԭ��Ĳ�˽������������[_Off]
    //����ԭ�������������ɵ�ƽ���ı������
    double operator *(const point &_Off) const
    {
        return x * _Off.y - y * _Off.x;
    }
    //���ƫ��
    point operator - (const point &_Off) const
    {
        return point(x - _Off.x, y - _Off.y);
    }
    //��λ����ͬ(double����)
    bool operator == (const point &_Off) const
    {
        return fabs(_Off.x - x) < eps && fabs(_Off.y - y) < eps;
    }
    //��λ�ò�ͬ(double����)
    bool operator != (const point &_Off) const
    {
        return ((*this) == _Off) == false;
    }
    //���������ƽ��
    double dis2(const point &_Off) const
    {
        return (x - _Off.x) * (x - _Off.x) + (y - _Off.y) * (y - _Off.y);
    }
    //��������
    double dis(const point &_Off) const
    {
        return sqrt((x - _Off.x) * (x - _Off.x) + (y - _Off.y) * (y - _Off.y));
    }
};

//�����ʾ������
class pVector
{
public:
    point s, e;//�����ʾ�����[s]���յ�[e]
    double a, b, c;//һ��ʽ,ax+by+c=0

    pVector(){}
    pVector(const point &s, const point &e):s(s),e(e){}

    //�������Ĳ��,��������[_Off]
    //[���������λ���ж�]
    double operator *(const point &_Off) const
    {
        return (_Off.y - s.y) * (e.x - s.x) - (_Off.x - s.x) * (e.y - s.y);
    }
    //�����������Ĳ��,����������[_Off]
    double operator *(const pVector &_Off) const
    {
        return (e.x - s.x) * (_Off.e.y - _Off.s.y) - (e.y - s.y) * (_Off.e.x - _Off.s.x);
    }
    //�������ʾת��Ϊһ���ʾ
    bool pton()
    {
        a = s.y - e.y;
        b = e.x - s.x;
        c = s.x * e.y - s.y * e.x;
        return true;
    }

    //-----------���ֱ�ߣ�������-----------
    //����������ߣ��ұߵ�С�ںŸĳɴ��ںż���,�ڶ�Ӧֱ���������=�ţ�
    //��������[_Off],����[_Ori]
    friend bool operator<(const point &_Off, const pVector &_Ori)
    {
        return (_Ori.e.y - _Ori.s.y) * (_Off.x - _Ori.s.x)
            < (_Off.y - _Ori.s.y) * (_Ori.e.x - _Ori.s.x);
    }

    //����ֱ����,��������[_Off]
    bool lhas(const point &_Off) const
    {
        return fabs((*this) * _Off) < eps;
    }
    //�����߶���,��������[_Off]
    bool shas(const point &_Off) const
    {
        return lhas(_Off)
            && _Off.x - min(s.x, e.x) > -eps && _Off.x - max(s.x, e.x) < eps
            && _Off.y - min(s.y, e.y) > -eps && _Off.y - max(s.y, e.y) < eps;
    }

    //�㵽ֱ��/�߶εľ���
    //������ ��[_Off], �Ƿ����߶�[isSegment](Ĭ��Ϊֱ��)
    double dis(const point &_Off, bool isSegment = false)
    {
        //��Ϊһ��ʽ
        pton();

        //��ֱ�ߴ���ľ���
        double td = (a * _Off.x + b * _Off.y + c) / sqrt(a * a + b * b);

        //������߶��жϴ���
        if(isSegment)
        {
            double xp = (b * b * _Off.x - a * b * _Off.y - a * c) / ( a * a + b * b);
            double yp = (-a * b * _Off.x + a * a * _Off.y - b * c) / (a * a + b * b);
            double xb = max(s.x, e.x);
            double yb = max(s.y, e.y);
            double xs = s.x + e.x - xb;
            double ys = s.y + e.y - yb;
            if(xp > xb + eps || xp < xs - eps || yp > yb + eps || yp < ys - eps)
                td = min(_Off.dis(s), _Off.dis(e));
        }

        return fabs(td);
    }

    //����ֱ�߶ԳƵĵ�
    point mirror(const point &_Off) const
    {
        //ע����תΪһ��ʽ
        point ret;
        double d = a * a + b * b;
        ret.x = (b * b * _Off.x - a * a * _Off.x - 2 * a * b * _Off.y - 2 * a * c) / d;
        ret.y = (a * a * _Off.y - b * b * _Off.y - 2 * a * b * _Off.x - 2 * b * c) / d;
        return ret;
    }
    //����������д���
    static pVector ppline(const point &_a, const point &_b)
    {
        pVector ret;
        ret.s.x = (_a.x + _b.x) / 2;
        ret.s.y = (_a.y + _b.y) / 2;
        //һ��ʽ
        ret.a = _b.x - _a.x;
        ret.b = _b.y - _a.y;
        ret.c = (_a.y - _b.y) * ret.s.y + (_a.x - _b.x) * ret.s.x;
        //����ʽ
        if(fabs(ret.a) > eps)
        {
            ret.e.y = 0.0;
            ret.e.x = - ret.c / ret.a;
            if(ret.e == ret. s)
            {
                ret.e.y = 1e10;
                ret.e.x = - (ret.c - ret.b * ret.e.y) / ret.a;
            }
        }
        else
        {
            ret.e.x = 0.0;
            ret.e.y = - ret.c / ret.b;
            if(ret.e == ret. s)
            {
                ret.e.x = 1e10;
                ret.e.y = - (ret.c - ret.a * ret.e.x) / ret.b;
            }
        }
        return ret;
    }

    //------------ֱ�ߺ�ֱ�ߣ�������-------------
    //ֱ���غ�,������ֱ������[_Off]
    bool equal(const pVector &_Off) const
    {
        return lhas(_Off.e) && lhas(_Off.s);
    }
    //ֱ��ƽ�У�������ֱ������[_Off]
    bool parallel(const pVector &_Off) const
    {
        return fabs((*this) * _Off) < eps;
    }
    //��ֱ�߽��㣬������Ŀ��ֱ��[_Off]
    point crossLPt(pVector _Off)
    {
        //ע�����ж�ƽ�к��غ�
        point ret = s;
        double t = ((s.x - _Off.s.x) * (_Off.s.y - _Off.e.y) - (s.y - _Off.s.y) * (_Off.s.x - _Off.e.x))
                / ((s.x - e.x) * (_Off.s.y - _Off.e.y) - (s.y - e.y) * (_Off.s.x - _Off.e.x));
        ret.x += (e.x - s.x) * t;
        ret.y += (e.y - s.y) * t;
        return ret;
    }

    //------------�߶κ�ֱ�ߣ�������----------
    //�߶κ�ֱ�߽�
    //�������߶�[_Off]
    bool crossSL(const pVector &_Off) const
    {
        double rs = (*this) * _Off.s;
        double re = (*this) * _Off.e;
        return rs * re < eps;
    }

    //------------�߶κ��߶Σ�������----------
    //�ж��߶��Ƿ��ཻ(ע�����eps)���������߶�[_Off]
    bool isCrossSS(const pVector &_Off) const
    {
        //1.�����ų������ж��������߶�Ϊ�Խ��ߵ����������Ƿ��ཻ
        //2.�������飨����0ʱ�˵��غϣ�
        return (
            (max(s.x, e.x) >= min(_Off.s.x, _Off.e.x)) &&
            (max(_Off.s.x, _Off.e.x) >= min(s.x, e.x)) &&
            (max(s.y, e.y) >= min(_Off.s.y, _Off.e.y)) &&
            (max(_Off.s.y, _Off.e.y) >= min(s.y, e.y)) &&
            ((pVector(_Off.s, s) * _Off) * (_Off * pVector(_Off.s, e)) >= 0.0) &&
            ((pVector(s, _Off.s) * (*this)) * ((*this) * pVector(s, _Off.e)) >= 0.0)
            );
    }
}t1,t2;

class polygon
{
public:
    const static long maxpn = N;
    point pt[maxpn];//�㣨˳ʱ�����ʱ�룩
    long n;//��ĸ���
    point& operator[](int _p)
    {
        return pt[_p];
    }

    //�����������������ڵ����˳ʱ�����ʱ��
    double area() const
    {
        double ans = 0.0;
        int i;
        for(i = 0; i < n; i ++)
        {
            int nt = (i + 1) % n;
            ans += pt[i].x * pt[nt].y - pt[nt].x * pt[i].y;
        }
        return fabs(ans / 2.0);
    }
    //���������ģ�������ڵ����˳ʱ�����ʱ��
    point gravity() const
    {
        point ans;
        ans.x = ans.y = 0.0;
        int i;
        double area = 0.0;
        for(i = 0; i < n; i ++)
        {
            int nt = (i + 1) % n;
            double tp = pt[i].x * pt[nt].y - pt[nt].x * pt[i].y;
            area += tp;
            ans.x += tp * (pt[i].x + pt[nt].x);
            ans.y += tp * (pt[i].y + pt[nt].y);
        }
        ans.x /= 3 * area;
        ans.y /= 3 * area;
        return ans;
    }
    //�жϵ���͹������ڣ���������[_Off]
    bool chas(const point &_Off) const
    {
        double tp = 0, np;
        int i;
        for(i = 0; i < n; i ++)
        {
            np = pVector(pt[i], pt[(i + 1) % n]) * _Off;
            if(tp * np < -eps)
                return false;
            tp = (fabs(np) > eps)?np: tp;
        }
        return true;
    }
    //�жϵ��Ƿ�������������[���߷�]��O(n)
    bool ahas(const point &_Off) const
    {
        int ret = 0;
        double infv = 1e-10;//����ϵ���Χ
        pVector l = pVector(_Off, point( -infv ,_Off.y));
        for(int i = 0; i < n; i ++)
        {
            pVector ln = pVector(pt[i], pt[(i + 1) % n]);
            if(fabs(ln.s.y - ln.e.y) > eps)
            {
                point tp = (ln.s.y > ln.e.y)? ln.s: ln.e;
                if(fabs(tp.y - _Off.y) < eps && tp.x < _Off.x + eps)
                    ret ++;
            }
            else if(ln.isCrossSS(l))
                ret ++;
        }
        return (ret % 2 == 1);
    }
    //͹����α�ֱ�߷ָ�,������ֱ��[_Off]
    polygon split(pVector _Off)
    {
        //ע��ȷ��������ܱ��ָ�
        polygon ret;
        point spt[2];
        double tp = 0.0, np;
        bool flag = true;
        int i, pn = 0, spn = 0;
        for(i = 0; i < n; i ++)
        {
            if(flag)
                pt[pn ++] = pt[i];
            else
                ret.pt[ret.n ++] = pt[i];
            np = _Off * pt[(i + 1) % n];
            if(tp * np < -eps)
            {
                flag = !flag;
                spt[spn ++] = _Off.crossLPt(pVector(pt[i], pt[(i + 1) % n]));
            }
            tp = (fabs(np) > eps)?np: tp;
        }
        ret.pt[ret.n ++] = spt[0];
        ret.pt[ret.n ++] = spt[1];
        n = pn;
        return ret;
    }

    //-------------͹��-------------
    //Grahamɨ�跨�����Ӷ�O(nlg(n)),���Ϊ��ʱ��
    //#include <algorithm>
    static bool graham_cmp(const point &l, const point &r)//͹��������
    {
        return l.y < r.y || (l.y == r.y && l.x < r.x);
    }
    polygon& graham(point _p[], int _n)
    {
        int i, len;
        sort(_p, _p + _n, polygon::graham_cmp);
        n = 1;
        pt[0] = _p[0], pt[1] = _p[1];
        for(i = 2; i < _n; i ++)
        {
            while(n && point::xmult(_p[i], pt[n], pt[n - 1]) >= 0)
                n --;
            pt[++ n] = _p[i];
        }
        len = n;
        pt[++ n] = _p[_n - 2];
        for(i = _n - 3; i >= 0; i --)
        {
            while(n != len && point::xmult(_p[i], pt[n], pt[n - 1]) >= 0)
                n --;
            pt[++ n] = _p[i];
        }
        return (*this);
    }

    //͹����ת����(ע������˳ʱ�����ʱ������)
    //����ֵ͹��ֱ����ƽ������Զ��������ƽ����
    double rotating_calipers()
    {
        int i = 1;
        double ret = 0.0;
        pt[n] = pt[0];
        for(int j = 0; j < n; j ++)
        {
            while(fabs(point::xmult(pt[j], pt[j + 1], pt[i + 1])) > fabs(point::xmult(pt[j], pt[j + 1], pt[i])) + eps)
                i = (i + 1) % n;
            //pt[i]��pt[j],pt[i + 1]��pt[j + 1]�����Ƕ����
            ret = max(ret, max(pt[i].dis(pt[j]), pt[i + 1].dis(pt[j + 1])));
        }
        return ret;
    }

    //͹����ת����(ע��������ʱ������)
    //����ֵ��͹������̾���
    double rotating_calipers(polygon &_Off)
    {
        int i = 0;
        double ret = 1e10;//inf
        pt[n] = pt[0];
        _Off.pt[_Off.n] = _Off.pt[0];
        //ע��͹��������ʱ��������pt[0]�����½ǵ��λ��
        while(_Off.pt[i + 1].y > _Off.pt[i].y)
            i = (i + 1) % _Off.n;
        for(int j = 0; j < n; j ++)
        {
            double tp;
            //��ʱ��ʱΪ >,˳ʱ�����෴
            while((tp = point::xmult(pt[j], pt[j + 1], _Off.pt[i + 1]) - point::xmult( pt[j], pt[j + 1], _Off.pt[i])) > eps)
                i = (i + 1) % _Off.n;
            //(pt[i],pt[i+1])��(_Off.pt[j],_Off.pt[j + 1])����������߶�
            ret = min(ret, pVector(pt[j], pt[j + 1]).dis(_Off.pt[i], true));
            ret = min(ret, pVector(_Off.pt[i], _Off.pt[i + 1]).dis(pt[j + 1], true));
            if(tp > -eps)//���������TLE������ò�Ҫ������ж�
            {
                ret = min(ret, pVector(pt[j], pt[j + 1]).dis(_Off.pt[i + 1], true));
                ret = min(ret, pVector(_Off.pt[i], _Off.pt[i + 1]).dis(pt[j], true));
            }
        }
        return ret;
    }

    //-----------��ƽ�潻-------------
    //���Ӷ�:O(nlog2(n))
    //#include <algorithm>
    //��ƽ����㼫�Ǻ���[�������Ч�ʿ����ó�Ա������¼]
    static double hpc_pa(const pVector &_Off)
    {
        return atan2(_Off.e.y - _Off.s.y, _Off.e.x - _Off.s.x);
    }
    //��ƽ�潻������[����˳��: 1.���� 2.ǰ���ֱ���ں�������]
    static bool hpc_cmp(const pVector &l, const pVector &r)
    {
        double lp = hpc_pa(l), rp = hpc_pa(r);
        if(fabs(lp - rp) > eps)
            return lp < rp;
        return point::xmult(l.s, r.e, r.s) < 0.0;
    }
    //���ڼ����˫�˶���
    pVector dequeue[maxpn];
    //��ȡ��ƽ�潻�Ķ���Σ�����εĺˣ�
    //��������������[l]����������[ln];(��ƽ�淽����������ߣ�
    //�������к����n[�����ض���εĵ�����]Ϊ0�򲻴��ڰ�ƽ�潻�Ķ���Σ������������������������
    polygon& halfPanelCross(pVector _Off[], int ln)
    {
        int i, tn;
        n = 0;
        sort(_Off, _Off + ln, hpc_cmp);
        //ƽ����������ߵ�ɸѡ
        for(i = tn = 1; i < ln; i ++)
            if(fabs(hpc_pa(_Off[i]) - hpc_pa(_Off[i - 1])) > eps)
                _Off[tn ++] = _Off[i];
        ln = tn;
        int bot = 0, top = 1;
        dequeue[0] = _Off[0];
        dequeue[1] = _Off[1];
        for(i = 2; i < ln; i ++)
        {
            if(dequeue[top].parallel(dequeue[top - 1]) ||
                dequeue[bot].parallel(dequeue[bot + 1]))
                return (*this);
            while(bot < top &&
                point::xmult(dequeue[top].crossLPt(dequeue[top - 1]), _Off[i].e, _Off[i].s) > eps)
                top --;
            while(bot < top &&
                point::xmult(dequeue[bot].crossLPt(dequeue[bot + 1]), _Off[i].e, _Off[i].s) > eps)
                bot ++;
            dequeue[++ top] = _Off[i];
        }

        while(bot < top &&
            point::xmult(dequeue[top].crossLPt(dequeue[top - 1]), dequeue[bot].e, dequeue[bot].s) > eps)
            top --;
        while(bot < top &&
            point::xmult(dequeue[bot].crossLPt(dequeue[bot + 1]), dequeue[top].e, dequeue[top].s) > eps)
            bot ++;
        //���㽻��(ע�ⲻֱͬ���γɵĽ�������غ�)
        if(top <= bot + 1)
            return (*this);
        for(i = bot; i < top; i ++)
            pt[n ++] = dequeue[i].crossLPt(dequeue[i + 1]);
        if(bot < top + 1)
            pt[n ++] = dequeue[bot].crossLPt(dequeue[top]);
        return (*this);
    }
}a;
point p[N];
int n;
double cal(int i,int j,int k)
{
    double x=a.pt[i].dis(a.pt[j]);
    double y=a.pt[j].dis(a.pt[k]);
    double z=a.pt[k].dis(a.pt[i]);
    double p=(x+y+z)/2;
    return sqrt(p*(p-x)*(p-y)*(p-z));
}
void init()
{
    for(int i=0;i<n;i++) scanf("%lf%lf",&p[i].x,&p[i].y);
    a=a.graham(p,n);
    double ans=0;
//    cout<<a.n<<endl;
//    for(int i=0;i<a.n;i++) printf("%.1f %.1f\n",a.pt[i].x,a.pt[i].y);
    for(int i=0;i<a.n-2;i++)
    {
        int k=i+2;
        for(int j=i+1;j<a.n-1;j++)
        {
            if(k==j) k++;
            while(k+1<a.n&&cal(i,j,k)<cal(i,j,k+1)) k++;
            ans=max(ans,cal(i,j,k));
        }
    }
    printf("%.2f\n",ans);
}
int main()
{
  //  freopen("in.txt","r",stdin);
    while(scanf("%d",&n),~n)
    {
        init();
    }
    return 0;
}