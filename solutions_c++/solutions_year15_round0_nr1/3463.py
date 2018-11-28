#include <bits/stdc++.h>
/*
 It's opening night at the opera, and your friend is the prima donna (the lead female singer).
 You will not be in the audience, but you want to make sure she receives a standing ovation --
 with every audience member standing up and clapping their hands for her.

Initially, the entire audience is seated. Everyone in the audience has a shyness level.
An audience member with shyness level Si will wait until at least Si other audience members have already stood
up to clap, and if so, she will immediately stand up and clap. If Si = 0, then the audience member will always
stand up and clap immediately, regardless of what anyone else does. For example, an audience member with Si = 2
will be seated at the beginning, but will stand up to clap later after she sees at least two other people standing
and clapping.

You know the shyness level of everyone in the audience, and you are prepared to invite additional friends of the
 prima donna to be in the audience to ensure that everyone in the crowd stands up and claps in the end. Each of
 these friends may have any shyness value that you wish, not necessarily the same. What is the minimum number of
 friends that you need to invite to guarantee a standing ovation?
Input

The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line
 with Smax, the maximum shyness level of the shyest person in the audience, followed by a string of Smax + 1
 single digits. The kth digit of this string (counting starting from 0) represents how many people in the audience
 have shyness level k. For example, the string "409" would mean that there were four audience members with Si = 0
 and nine audience members with Si = 2 (and none with Si = 1 or any other value). Note that there will initially
 always be between 0 and 9 people with each shyness level.

The string will never end in a 0. Note that this implies that there will always be at least one person in
the audience.
*/
using namespace std;

int main(int argc,char** argv)
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int cases,maxshy;
    vector<int> shyness_p;
    string pers_vec_str;

    cin>>cases;
    int n_friend;

    for(int i=0;i<cases;i++)
    {
        shyness_p.clear();
        n_friend = 0;
        cin>>maxshy;
        cin>>pers_vec_str;
        for(int k=0;k<=maxshy;k++)
        {
            shyness_p.push_back((int)pers_vec_str[k]-48);

        }

        int s_shyness = shyness_p[0];

        for(int j=1;j<shyness_p.size();j++)
        {
            if((s_shyness-j)<0 && shyness_p[j]!=0)
            {
                n_friend += abs(s_shyness-j);

                s_shyness+= abs((s_shyness-j));
                s_shyness+= shyness_p[j];
            }
            else
                s_shyness += shyness_p[j];
        }

        cout<<"Case #"<<i+1<<": "<<n_friend<<endl;
        s_shyness=0;


    }

    return EXIT_SUCCESS;
}
