//Even the strongest of opponents always has a weakness.

//No single thing is perfect by itself. That's why we're born to attract other things to make up for what we lack.
//I think we start walking in the right direction only after we start getting our counterparts beside us.

//It's never been "The one who becomes Hokage will be acknowledge by everyone",
// it's "The one who is acknowledge by everyone, becomes the Hokage".

//Growth occurs when one goes beyond one's limits. Realizing that is also part of training.

//Those who turn their hands against their comrades are sure to die a terrible death. Be prepared.

//You are weak. Why are you so weak? Because you lack... hatred.

//- Itachi Uchiha

//Tears and rain, fall down on my face, my body is unable to stay yet my heart is unwilling to leave.

// My name is Sasuke Uchiha. I hate a lot of things, and I don't particularly like anything.
//What I have is not a dream, because I will make it a reality.
//I'm going to restore my clan, and kill a certain someone.

//- sasuke uchiha
#include <bits/stdc++.h>

using namespace std;

int n,a[100005];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("outputl.txt", "w", stdout);
    int t;
    cin>>t;
    int cases = 1;
    while(t--)
    {
        int x,ans,sum;
        string y;
        cin>>x>>y;
        ans = sum =  0;
        for(int i = 0; i < y.size(); i++)
        {
            if( sum >= i)
            {
                ;
            }
            else {
                ans = ans + (i-sum);
                sum= sum + ( i - sum);
            }
            sum = sum + (y[i] - '0');
        }

        cout<<"Case #"<<cases<<":"<<" "<<ans<<endl;
        cases++;
    }
    return 0;
}

