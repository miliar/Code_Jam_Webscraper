#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int encontraVal(vector<double> v,double val)
{
    int tam = v.size();
    for(int i=0;i<tam;i++)
    {
        if(v[i]==val)
        return 1;
    }
    return 0;
}

int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        int T;
        cin>>T;
        vector<double> vN;
        vector<double> vK;
        double v1,v2;
        for(int j=0;j<T;j++)
        {
            cin>>v1;
            vN.push_back(v1);
        }
        for(int j=0;j<T;j++)
        {
            cin>>v2;
            vK.push_back(v2);
        }
        std::sort(vN.begin(), vN.end());
        std::sort(vK.begin(), vK.end());
        int wK=0,wN=0;
        vector<double>aux;
        aux = vN;
        for(int j=0;j<T;j++)
        {
            for(int h=0;h<T;h++)
            {
                if(aux[h]<vK[j] && aux[h]!=-1)
                {
                    wK++;
                    aux[h]=-1;
                    j++;

                }
            }
        }
        wN = T-wK;
        int wdN=0;
        if(T==1 && vN[0]>vK[0])
        wdN++;
        else
        for(int hz=0;hz<T;hz++)
        {
            for(int tz=0;tz<T;tz++)
            {
                if(vN[hz]>vK[tz] && vK[tz]!=-1)
                {
                    vK[tz]=-1;
                    wdN++;
                    hz++;

                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<wdN<<" "<<wN<<endl;


    }
    return 0;
}
