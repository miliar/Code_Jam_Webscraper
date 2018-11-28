#include <iostream>
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class QCat
{
public:
    int n,i,j,k;
    QCat():
        n(0),i(0),j(0),k(0)
    {

    };
    QCat(char c):
        n(0),i(0),j(0),k(0)
    {
        switch(c)
        {
        case 'i':
            i=1;
            break;
        case 'j':
            j=1;
            break;
        case 'k':
            k=1;
            break;
       default:
            n=1;
            break;
        }
    }
    QCat(int a,int b,int c,int d):
        n(a),i(b),j(c),k(d)
    {

    };
    const QCat operator*(const QCat& mul)
    {
#define mu1(l) (l)*mul.l
#define mu2(l,r) (l)*mul.r
        QCat out;
        //mu1(i);
        out.n=mu1(n)-mu1(i)-mu1(j)-mu1(k);
        out.i=mu2(i,n)+mu2(n,i)+mu2(j,k)-mu2(k,j);
        out.j=mu2(n,j)-mu2(i,k)+mu2(j,n)+mu2(k,i);
        out.k=mu2(n,k)+mu2(k,n)+mu2(i,j)-mu2(j,i);
        return out;
    }
    const bool operator==(const QCat& mul)
    {
        if(n!=mul.n)
            return false;
        if(i!=mul.i)
            return false;
        if(j!=mul.j)
            return false;
        if(k!=mul.k)
            return false;
        return true;
    }

};
std::ostream& operator<<(std::ostream& os, const QCat& q)
{
        if(q.n!=0)
        os<<q.n<<" ";
        if(q.i!=0)
        os<<q.i<<"i";
        if(q.j!=0)
        os<<q.j<<"j";
        if(q.k!=0)
        os<<q.k<<"k";
  // write obj to stream
  return os;
}

bool solve2(char *buf,int l,int L)
{

    const static QCat I('i'),J('j'),K('k');
    static QCat mas[10100][10010];
    for(int i=0;i<l;i++)
        mas[0][i]=QCat(buf[i%L]);
    for(int j=1;j<l;j++)
    {
        for(int i=0;i<l-j;i++)
        {
            mas[j][i]=mas[j-1][i]*mas[0][i+j];
           // cout<< mas[j][i]<<'\t';
        }
        //cout<<endl;
    }
    for(int i=0;i<l;i++)
    {
        if(mas[i][0]==I)
        {
            //cout<<"findi "<<i<<endl;;
            for(int j=0;j<l-i-1;j++)

                if(mas[j][i+1]==J){

                //cout<<"findj "<<j<<endl;
                    //for(int k=0;k<l-j-i-1;k++){
                        if(mas[l-j-i-2-1][i+j+2]==K){

                            //cout<<"findk "<<l-j-i-2<<endl;
                            return true;
                            }
                   //         return true;}
                }
        }
    }
    return false;
}
bool solve(char *buf,int l,int L)
{
    const static QCat I('i'),J('j'),K('k');
    QCat now(buf[0]);
    for(int i=1;i<l;i++)
    {
        if(!(now==I))
        {
            now=now*QCat(buf[i%L]);
            //cout<<"now="<<now<<endl;
            continue;
        }
        //cout<<"!now="<<now<<"I="<<I<<endl;
        QCat sec=QCat(buf[i%L]);
        for(int j=i;j<l;j++)
        {
            if(!(sec==J))
            {
                sec=sec*QCat(buf[j%L]);
                continue;
            }
            //cout<<"!sec="<<sec<<"J="<<J<<endl;
            QCat th=QCat(buf[j%L]);
            int k=j+1;
            for(k=j+1;k<l;k++)
            {
                th=th*QCat(buf[k%L]);
            }
            if(th==K){
                    cout<<"answer "<<i<<" "<<j<<" "<<k<<" ";
                return true;
            }
        }
    }
    return false;
}
int main()
{
    //ofstream out("C-small.out");
    ofstream out("C-small-attempt2.out");
    //ifstream in("C-small.in");
    ifstream in("C-small-attempt2.in");
    QCat a(0,1,0,0);
    QCat b(0,0,0,1);
    cout<<a<<"*"<<b<<"="<<a*b<<endl;
#define cin in
#define cout out
    int T;
    cin>>T;
    for(int i=0;i<T;i++)
    {
        char buf[10010];
        char buf1[10010];
        int L,X;
        cin>>L>>X;
        cin>>buf1;
        sprintf(buf,"%s",buf1);
        /*for(int j=1;j<X;j++)
            sprintf(buf,"%s%s",buf,buf1);*/
        printf("%i\n",i);
        //cout<<buf<<endl;
        //bool a1=solve2(buf,L*X,L);
        //bool a2=solve(buf,L*X,L);
        //if(a1!=a2)
        //    printf("\n!!!!!!!!!!\nCase #%i\n!!!!!!!!!!\n",i+1);
        cout<<"Case #"<<i+1<<": "<<(solve2(buf,L*X,L)?"YES":"NO")<<"\n";
        //cout<<"Case #"<<i+1<<": "<<(solve(buf,L*X,L)?"YES":"NO")<<"\n";

    }
    //cout << "Hello world!" << endl;
    return 0;
}
