#include<bits/stdc++.h>
using namespace std;

struct info{
    int a;
    int pos;

}kk[100];

bool comp(info a,info b)
{
    return a.a>b.a;
}

int main()
{
    freopen("0in.txt","r",stdin);
    freopen("0out.txt","w",stdout);
    int i,j,k,t,num,s;
    scanf("%d",&t);

    for(int kk1=1;kk1<=t;kk1++)
    {
        scanf("%d",&num);
        for(i=0;i<=26;i++)
        {
            kk[i].a=0;
            kk[i].pos=0;
        }


        for(i=0;i<num;i++)
        {
            scanf("%d",&s);
            kk[i].a=s;
            kk[i].pos=i+65;
        }

        vector<string>vec;
        string aa="";
        string bb="";
        string ss="";


        while(1)
        {
            sort(kk,kk+num,comp);
            if(kk[0].a==0)
            {
                break;
            }

            if(kk[0].a!=0&&kk[1].a!=0)
            {
                //cout<<(char)(kk[0].pos)<<(char)(kk[1].pos)<<" ";
                aa="";
                bb="";
                ss="";
                aa=(char)(kk[0].pos);
                bb=(char)(kk[1].pos);
                ss=aa+bb;
                vec.push_back(ss);
                kk[0].a--;
                kk[1].a--;


            }

             else if(kk[0].a!=0&&kk[1].a==0)
            {
                 aa="";
                 bb="";
                 ss="";

                if(kk[0].a==1)
                {
                    aa=(char)(kk[0].pos);
                    vec.push_back(aa);
                    kk[0].a--;
                }
                else
                {
                    aa=(char)(kk[0].pos);
                    bb=(char)(kk[0].pos);
                    ss=aa+bb;
                    vec.push_back(ss);
                    kk[0].a--;
                    kk[0].a--;
                }

            }






        }

        //cout<<vec.size()<<endl;
        printf("Case #%d: ",kk1);
        string pp="",qq="";
        int len=vec.size();
        if(len>=2){
        pp=vec[len-1];
        qq=vec[len-2];
        if(pp.size()==1)
        {
            vec[len-2]=pp;
            vec[len-1]=qq;
        }


        }

        for(i=0;i<vec.size();i++)
        {
            cout<<vec[i]<<" ";
        }
        cout<<endl;


    }




}
