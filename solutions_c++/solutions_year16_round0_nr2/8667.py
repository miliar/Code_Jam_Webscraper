#include<bits/stdc++.h>

typedef long long ll;

using namespace std;

string str;

void solve(ll tc)
{
    ll N, the_previous, i, positive_cnt, negetive_cnt, ans;

    the_previous = 0;
    N = str.length();
    for(i = 1;i < N;++i)
    {
        if(str[i] == str[the_previous])
        {
            continue;
        }
        else
        {
            ++the_previous;
            str[the_previous] = str[i];
        }
    }

    ++the_previous;
    positive_cnt = negetive_cnt = 0;
    for(i = 0;i < the_previous;++i)
    {
        if(str[i] == '+')
        ++positive_cnt;
        else
        ++negetive_cnt;
    }

    //printf("Case #%lld: ", tc);

    if((positive_cnt == 0) && (the_previous & 1))
    {
        ans = 1;
    }
    else if((negetive_cnt == 0) && (the_previous & 1))
    {
        ans = 0;
    }
    else if((positive_cnt > negetive_cnt) && (the_previous & 1))
    {
        ans = the_previous - 1;
    }
    else if(the_previous & 1)
    {
        ans = the_previous;
    }
    else
    {
        if(positive_cnt == 0){
            ans = 1;
        } else if(negetive_cnt == 0){
            ans = 0;
        } else if(str[0] == '+'){
            ans = the_previous;
        } else {
            ans = the_previous - 1;
        }
    }

    printf("Case #%lld: %lld\n", tc, ans);

}

int main(){
	ll t;
	cin >> t;
	for(ll tc = 1;tc <= t;++tc){
		cin>>str;
        solve(tc);
	}
	return 0;
}
