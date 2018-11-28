#include <iostream>
#include<fstream>

using namespace std;

class digits_seen
{
    public:
    digits_seen() {for(int i=0;i<10;i++){seen[i]=false;}}
    bool all_seen() const {for(int i=0;i<10;i++){if(!seen[i]) return false;} return true;}
    void update(long);
    private:
    void set_seen(int d) {seen[d]=true;}
    bool seen[10];
};

void digits_seen::update(long N)
{
    if(N<10)
    {
        set_seen(N);
        return;
    }
    else
    {
        while(N>0)
        {
            set_seen(N%10);
            N=N/10;
        }
    }
}

int main()
{
    ifstream in;
    in.open("in.in");
    ofstream out;
    out.open("out.txt");
    long T,N,i,cur;
    in>>T;
    for(i=1;i<=T;i++)
    {
        in>>N;
        if(N==0)
        {
            out<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        }
        else
        {
            cur=N;
            //j=1;
            digits_seen ds;
            ds.update(cur);
            while(!ds.all_seen())
            {
                cur+=N;
                ds.update(cur);
            }
            out<<"Case #"<<i<<": "<<cur<<endl;
        }
    }
    in.close();
    out.close();

}
