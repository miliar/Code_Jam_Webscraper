#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <list>
#include <algorithm>
using namespace std;
list<double> NsB;
vector<double> KsB;
vector<double> NsBv;
list<double> KsBl;
int nPoint, kPoint;

void war()
{
    for(vector<double>::iterator ni = NsBv.begin();  ni!=NsBv.end(); ++ni)
    {
        bool kWin = false;
        for(list<double>::iterator ki = KsBl.begin(); ki!=KsBl.end(); ++ki)
        {
            if((*ki)>(*ni))
            {
                kWin =true;
                ++kPoint;
                KsBl.erase(ki);                
                break;
            }
        }
        if(!kWin)
        {
            ++nPoint;
            KsBl.pop_front();
        }
    }
}

void d_war()
{
    for(vector<double>::iterator ki = KsB.begin();  ki!=KsB.end(); ++ki)
    {
        bool nWin = false;
        for(list<double>::iterator ni = NsB.begin(); ni!=NsB.end(); ++ni)
        {
            if((*ni)>(*ki))
            {
                nWin =true;
                ++nPoint;
                NsB.erase(ni);                
                break;
            }
        }
        if(!nWin)
        {
            ++kPoint;
            NsB.pop_front();
        }
        //KsB.erase(ki);
    }
}
void main()
{
    //cout.setf(ios::fixed);
    //cout.precision(7);
    //cout << 3.12345 << endl;
    double tmp;
    int T;
    cin >> T;
    for(int C=0; C<T; ++C)
    {
        int N;
        cin >> N;
        NsB.clear();
        KsB.clear();
        NsBv.clear();
        KsBl.clear();
        for(int i=0; i<N; ++i)
        {            
            cin >> tmp;
            NsB.push_back(tmp);
            NsBv.push_back(tmp);
        }
        for(int i=0; i<N; ++i)
        {
            double tmp;
            cin >> tmp;
            KsB.push_back(tmp);
            KsBl.push_back(tmp);
        }

        nPoint=0;
        kPoint=0;
        NsB.sort();
        //KsB.sort();
        std::sort(KsB.begin(), KsB.end(), std::greater<double>());
        d_war();
        int d_warN = nPoint;
        sort(NsBv.begin(), NsBv.end());
        KsBl.sort();
        nPoint =0;
        kPoint =0;
        war();
        int warN = nPoint;
        cout << "Case #" << C+1 << ": ";
        cout << d_warN << " " << warN << endl;
        //
        
    }

}