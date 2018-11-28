#include <bits/stdc++.h>
#define mp make_pair
#define xx first
#define yy second
using namespace std;

multiset<pair<int,int> > st;
multiset<pair<int,int> > :: iterator it,it2,it3;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int n,t,a, cs=1;

    scanf("%d",&t);

    while(t--)
    {
        scanf("%d",&n);
        int sum=0;

        for(int i=0; i<n; i++)
        {
            scanf("%d",&a);
            st.insert(mp(a,i));
            sum+=a;
        }
        n=sum;
        printf("Case #%d: ",cs++);
        while(n>0)
        {
            it= st.end();
            it--;
            if(it!=st.begin())
            {
                it2=it;
                it--;

                pair<int,int> p1,p2, p3;
                p2= *it;
                p1= *it2;
//                printf("%d %d %d %d\n",p1.xx, p1.yy, p2.xx, p2.yy);

                if(p1.xx== p2.xx)
                {
                    if(it!=st.begin())
                    {
                        it3=it;
                        it3--;
                        p3= *it3;
                        if(p3.xx==p2.xx)
                        {
                            printf("%c ",p1.yy+'A');
                            p1.xx--;
                            st.erase(it2);
                            if(p1.xx>0)
                            {
                                st.insert(p1);
                            }
                            n--;
                            continue;
                        }
                    }
                    printf("%c%c",p1.yy+'A', p2.yy+'A');
                    p1.xx--;
                    p2.xx--;
                    st.erase(it);
                    st.erase(it2);
                    if(p1.xx>0)
                    {
                        printf(" ");
                        st.insert(p1);
                        st.insert(p2);
                    }
                }
                else
                {
                    printf("%c ",p1.yy+'A');
                    p1.xx--;
                    st.erase(it2);
                    if(p1.xx>0)
                    {
                        st.insert(p1);
                    }
                    n++;
                }
                n-=2;
            }
            else
            {
                pair<int,int>p= *it;
                if(p.xx>1)
                {
                    printf("%c%c",p.yy+'A');
                    p.xx-=2;
                    st.erase(it);

                    if(p.xx>0)
                    {
                        printf(" ");
                        st.insert(p);
                    }
                    n-=2;
                }
                else
                {
                    printf("%c",p.yy+'A');
                    n--;
                }
            }
//            printf("n %d\n",n);
        }
        st.clear();
        printf("\n");
    }
}
