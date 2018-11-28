#include<bits/stdc++.h>
using namespace std;
int main()
{
    int tt;
#ifndef ONLINE_JUDGE
    freopen("input.txt","r",stdin);
    freopen("out.txt","w",stdout);
#endif
    cin>>tt;
    for(int k=1; k<=tt; k++)
    {
        string str;
        cin>>str;
        int sz=str.length();
        int a[26];
        memset(a,0,sizeof(a));
        for(int i=0; i<sz; i++)
        {
            a[str[i] - 'A']++;
        }
        int cnt_0=0,cnt_1=0,cnt_2=0,cnt_3=0,cnt_4=0,cnt_5=0,cnt_6=0,cnt_7=0,cnt_8=0,cnt_9=0;
        //for unique number
        //for zero
        if(a['Z'-'A'] !=0 && a['E'-'A']!=0 && a['R'-'A']!=0 && a['O'-'A']!=0)
        {
            int mn=min(a['Z'-'A'],min(a['E'-'A'],min(a['R'-'A'],a['O'-'A'])));
            cnt_0=mn;
            a['E'-'A']-=mn;
            a['R'-'A']-=mn;
            a['O'-'A']-=mn;
            a['Z'-'A']-=mn;;
        }
        //for two
        if(a['W'-'A']!=0 && a['T'-'A']!=0 && a['O'-'A']!=0)
        {
            int mn=min(a['W'-'A'],min(a['T'-'A'],a['O'-'A']));
            cnt_2=mn;
            a['T'-'A']-=mn;
            a['O'-'A']-=mn;
            a['W'-'A']-=mn;
        }
        //for four
        if(a['U'-'A']!=0 && a['F'-'A']!=0 && a['O'-'A']!=0 && a['R'-'A']!=0)
        {

            int mn=min(a['U'-'A'],min(a['F'-'A'],min(a['O'-'A'],a['R'-'A'])));
            cnt_4=mn;
            a['F'-'A']-=mn;
            a['O'-'A']-=mn;
            a['R'-'A']-=mn;
            a['U'-'A']-=mn;
        }
        //after 4 if 0 exit then it can be only 1
        //for ONE
        if(a['O'-'A']!=0 && a['N'-'A']!=0 && a['E'-'A']!=0)
        {
            int mn=min(a['O'-'A'],min(a['N'-'A'],a['E'-'A']));
            cnt_1=mn;
            a['N'-'A']-=mn;
            a['E'-'A']-=mn;
            a['O'-'A']-=mn;
        }
        //if after 4 it R exisist then it would ne 3
        //for three
        if(a['R'-'A']!=0 && a['T'-'A']!=0 && a['H'-'A']!=0 && a['E'-'A']!=0)
        {
            int mn=min(a['R'-'A'],min(a['T'-'A'],min(a['H'-'A'],a['E'-'A']/2)));
            cnt_3=mn;
            a['T'-'A']-=mn;
            a['H'-'A']-=mn;
            a['E'-'A']-=mn;
            a['E'-'A']-=mn;
            a['R'-'A']-=mn;
        }

        //after 4 if F exit then it would be 5
        //for FIVE
        if(a['F'-'A']!=0 && a['I'-'A']!=0 && a['V'-'A']!=0 && a['E'-'A']!=0)
        {
            int mn=min(a['F'-'A'],min(a['I'-'A'],min(a['V'-'A'],a['E'-'A'])));
            cnt_5=mn;
            a['I'-'A']-=mn;
            a['V'-'A']-=mn;
            a['E'-'A']-=mn;
            a['F'-'A']-=mn;
        }
        //for six
        if(a['X'-'A']!=0 && a['S'-'A']!=0 && a['I'-'A']!=0)
        {
            int mn=min(a['X'-'A'],min(a['S'-'A'],a['I'-'A']));
            cnt_6=mn;
            a['S'-'A']-=mn;
            a['I'-'A']-=mn;
            a['X'-'A']-=mn;
        }
        //after 6 if S exit then it could be only 7
        //for seven
        if(a['S'-'A']!=0 && a['E'-'A']!=0 && a['V'-'A']!=0  && a['N'-'A']!=0)
        {
            int mn=min(a['S'-'A'],min(a['E'-'A']/2,min(a['V'-'A'],a['N'-'A'])));
            cnt_7=a['S'-'A'];
            a['E'-'A']-=a['S'-'A'];
            a['V'-'A']-=a['S'-'A'];
            a['E'-'A']-=a['S'-'A'];
            a['N'-'A']-=a['S'-'A'];
            a['S'-'A']=0;;

        }
        //after 7 if N exit it could be only 9
        //for nine
        if(a['N'-'A']!=0 && a['I'-'A']!=0 && a['E'-'A']!=0)
        {
            int mn=min(a['N'-'A']/2,min(a['I'-'A'],a['E'-'A']));
            cnt_9=mn;
            a['I'-'A']-=mn;
            a['E'-'A']-=mn;
            a['N'-'A']-=(2*mn);
        }
        //for eight
        if(a['G'-'A']!=0 && a['E'-'A']!=0 && a['I'-'A']!=0 && a['H'-'A']!=0 && a['T'-'A']!=0)
        {
            int mn=min(a['G'-'A'],min(a['E'-'A'],min(a['I'-'A'],min(a['H'-'A'],a['T'-'A']))));
            cnt_8=mn;
            a['E'-'A']-=mn;
            a['I'-'A']-=mn;
            a['H'-'A']-=mn;
            a['T'-'A']-=mn;
            a['G'-'A']-=mn;
        }
        cout<<"Case #"<<k<<": ";
        while(cnt_0!=0)
        {
            cout<<"0";
            cnt_0--;
        }
        while(cnt_1!=0)
        {
            cout<<"1";
            cnt_1--;
        }
        while(cnt_2!=0)
        {
            cout<<"2";
            cnt_2--;
        }
        while(cnt_3!=0)
        {
            cout<<"3";
            cnt_3--;
        }
        while(cnt_4!=0)
        {
            cout<<"4";
            cnt_4--;
        }
        while(cnt_5!=0)
        {
            cout<<"5";
            cnt_5--;
        }
        while(cnt_6!=0)
        {
            cout<<"6";
            cnt_6--;
        }
        while(cnt_7!=0)
        {
            cout<<"7";
            cnt_7--;
        }
        while(cnt_8!=0)
        {
            cout<<"8";
            cnt_8--;
        }
        while(cnt_9!=0)
        {
            cout<<"9";
            cnt_9--;
        }
        cout<<endl;
    }
    return 0;
}
