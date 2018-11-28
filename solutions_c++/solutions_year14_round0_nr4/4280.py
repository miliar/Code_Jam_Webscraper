#include<iostream>
#include<algorithm>
using namespace std;

int N;

int gao(int st1, int end1, int st2, int end2, double nao[], double ken[])
{
    if(st1 > end1 || st2 > end2) return 0;
    int ans = 0;
    while(st1 <= end1 && st2 <= end2 && nao[st1] < ken[st2])
    {
        st1++;
        end2--;
    }
    while(st1 <= end1 && st2 <= end2 && nao[st1] > ken[st2])
    {
        ans++;
        st1++;
        st2++;
    }
    return ans + gao(st1, end1, st2, end2, nao, ken);
}

int main()
{
    int Case;
    cin>>Case;
    for(int t = 1; t <= Case; t++)
    {
        cin>>N;
        double nao[1001],ken[1001];
        for(int i = 0; i < N; i++)
            cin>>nao[i];
        for(int i = 0; i < N; i++)
            cin>>ken[i];
        sort(nao, nao + N);
        sort(ken, ken + N);
        int ans0=0, ans1=0;
        /*
        int st = N-1;
        while(st >= 0 && ken[st] > nao[N-1]) st--;
        int cur = N-1;
        while(st >= 0)
        {
            if(nao[cur] > ken[st])
                ans0++;
            cur--;
            st--;
        }
        */
        ans0 = gao(0, N-1, 0, N-1, nao, ken);
        bool used[1001]={0};
        for(int i = N-1; i >= 0; i--)
        {
            bool flag = false;
            for(int j = 0; j < N; j++)
                if(ken[j] > nao[i] && !used[j])
                {
                    flag = true;
                    used[j] = true;
                    break;
                }
            if(!flag)
            {
                ans1++;
                for(int j=0; j < N; j++)
                    if(!used[j])
                    {
                        used[j] = true;
                        break;
                    }
            } 
        }
        cout<<"Case #"<<t<<": "<<ans0<<' '<<ans1<<endl;
    }
    return 0;
}
