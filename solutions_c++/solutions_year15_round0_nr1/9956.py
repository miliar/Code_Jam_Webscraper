#include <iostream>
#include <map>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.OT","w",stdout);
    map <unsigned int,unsigned int> aud;
    char c;
    int i,j;
    unsigned int friends_needed=0,t,max_shy,people_standing=0,counter=0;
    cin>>t;
    while(t--)
    {
        counter++;
        people_standing=0;
        friends_needed=0;
        max_shy=0;
        cin>>max_shy;
        for(i=0;i<=max_shy;i++)
        {
            cin>>c;
            j=c-'0';
            aud[i]=j;
        }
        for(i=0;i<=max_shy;i++)
        {
            if(people_standing>=i)
            {
                people_standing+=aud[i];
            }
            else
            {

                if(aud[i]>0)
                {
                    friends_needed+=(i-people_standing);
                    people_standing+=friends_needed;
                }
                people_standing+=aud[i];
            }
        }
        cout<<"Case #"<<counter<<": "<<friends_needed<<endl;
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}
