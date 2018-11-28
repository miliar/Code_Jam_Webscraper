#include<bits/stdc++.h>
using namespace std;
typedef long long lli;

int t,X,n,i,x,j;
std::vector<pair<int,int> >vec;
int main()
{
     freopen("inp.txt","r",stdin);
     freopen("out.txt","w",stdout);

    scanf("%d",&t);

    while(t--)
    {
        X++;
        printf("Case #%d: ",X);
        scanf("%d",&n);

        vec.clear();
        for(i=0; i<n; i++)
        {
            scanf("%d",&x);
            vec.push_back(make_pair(x,i));
        }

        sort(vec.begin(),vec.end());

        i=vec.size()-1;

        while(i>0)
        {
            while( vec[i].first>vec[i-1].first)
            {
                for(j=i; j<vec.size(); j++)
                {
                    printf("%c ",vec[j].second+65);
                    vec[j].first--;
                }
            }
            i--;
        }

        if(vec.size()==2)
        {
            while(vec[0].first>0)
                {printf("AB ");vec[0].first--;}
            printf("\n");
            continue;
        }

        while(vec[i].first>1)
        {
           for(j=i; j<vec.size(); j++)
                {
                    printf("%c ",vec[j].second+65);
                    vec[j].first--;
                }
        }

        if(vec.size()>3)
        {
            while(vec.size()>3)
            {
                printf("%c ",vec[vec.size()-1].second+65);
                vec.pop_back();
            }
            printf("%c ",vec[vec.size()-1].second+65);
            vec.pop_back();
            printf("%c%c\n",vec[vec.size()-1].second+65,vec[vec.size()-2].second+65);
        }
        else if(vec.size()==3)
        {
            printf("%c ",vec[vec.size()-1].second+65);
            vec.pop_back();
            printf("%c%c\n",vec[vec.size()-1].second+65,vec[vec.size()-2].second+65);
        }
        else if(vec.size()==2)
        {
            printf("%c%c\n",vec[vec.size()-1].second+65,vec[vec.size()-2].second+65);
        }
    }
    return 0;
}
