#include <bits/stdc++.h>

using namespace std;

int calctimesplit(vector<int>& vett, int livello)
{
    int time=0;

    for(int i = 0; i < vett.size(); i++)
    {
        if(vett[i] > livello)
        {
            if(vett[i]%livello == 0) time+=(vett[i]/livello)-1;
            else time+=(vett[i]/livello);
        }

    }
    time+=livello;

    return time;
}

int main(int argc,char** argv)
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int cases;

    cin>>cases;

    int n_persone;
    vector<int> plates;

    for(int i=0; i < cases; i++)
    {
        cin>>n_persone;
        plates.clear();
        for(int k = 0; k < n_persone; k++)
        {
            int buff;
            cin>>buff;
            plates.push_back(buff);
        }

        int time_no_div = *max_element(plates.begin(),plates.end());
        int timeapp=0;
        int timesplits = INT_MAX;
        int to = time_no_div;

        for(int k = 1; k <= to; k++)
        {
            timeapp = calctimesplit(plates,k);

            if(timeapp<timesplits) timesplits = timeapp;
        }
        if(time_no_div < timesplits) cout<<"Case #"<<i+1<<": "<<time_no_div<<endl;
        else cout<<"Case #"<<i+1<<": "<<timesplits<<endl;
    }

    return EXIT_SUCCESS;
}
