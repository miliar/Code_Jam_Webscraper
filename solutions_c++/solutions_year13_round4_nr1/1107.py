#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool isPrime[1000000];
vector<long long> prime;
void getPrime()
{
	for(long long i = 0; i < 1000000; i++)
	{
		isPrime[i] = true;
	}

	isPrime[0] = false;
	isPrime[1] = false;

	for(long long i = 2; i < 1000000; i++)
	{
		if(isPrime[i] == true)
		{
			prime.push_back(i);
			long long test = i * 2;
			while(test < 1000000)
			{
				isPrime[test] = false;
				test += i;
			}
		}
	}

}

bool compare(int a, int b)
{
	return(a < b);
}

void compare_sample()
{
	int myints[] = {32,71,12,45,26,80,53,33};
	vector<int> myvector (myints, myints+8);        
	vector<int>::iterator it;
	sort (myvector.begin()+4, myvector.end(), compare);
}
vector<vector<long long> > PT(502, vector<long long> (502, 1));

void create_pt()
{
	for(int i = 2; i <= 500; i++)
	{
		for(int j = 1; j < i; j++)
		{
			PT[i][j] = (PT[i-1][j-1] + PT[i-1][j]) % 100003;
		}
	}
}

long long c_x_get_y(long long x, long long y)
{
	if(y == 0)
		return 1;
	long long ans = 1;
	for(int i = 0; i < y; i++)
	{
		ans *= (x - i);
		ans /= (i + 1);
	}
	return ans;
}

long long price(long long n, long long x) {

    return ((n+n-x+1) * x / 2);

}

int main()
{
	char c;
	int data_num, case_count = 1;
	cin >> data_num;
	while(data_num != 0)
	{
		cout << "Case #" << case_count << ": ";
        long long N, M, o[1000], e[1000], p[1000], total1[100], total2[100];
        for(int i = 0; i < 100; i++) {
            total1[i] = 0;
            total2[i] = 0;
        }
        vector<vector<long long> > yoo;
        cin >> N >> M;
        long long ori = 0;
        long long after = 0;
        for(int i = 0; i < M; i++) {
            cin >> o[i] >> e[i] >> p[i];
            ori += price(N, e[i] - o[i]) * p[i];
            vector<long long> x;
            total1[e[i]-o[i]] += p[i];
            x.push_back(o[i]);
            x.push_back(e[i]);
            for(int j = 0; j < p[i]; j++) {
                yoo.push_back(x);
            }
        }
        //sort(yoo.begin(), yoo.end(), compare);
        //for(int i = 0; i < M; i++) {
        //    for(int j = 0; j < 3; j ++)
        //        cout << yoo[i][j] <<" ";
        //    cout << endl;
        //}
        //for(int i = 0; i < M; i++) {
        //    if(p[i] >0) {
        //    for(int j = i+1 ; j < M; j++) {
        //        if(o[i] < o[j] && o[j] <= e[i] && e[i] < e[j]) {
        //            
        //        }

        //    }
        //    }
        //}
        bool change = false;
        while(true) {
            for(long long i = 0; i < yoo.size(); i++) {
                for(long long j = 0; j < yoo.size(); j++) {
                    if(i != j) {
                    if(yoo[i][0] < yoo[j][0] && yoo[j][0] <= yoo[i][1] && yoo[i][1] < yoo[j][1]){
                        long long x = yoo[i][0];
                        yoo[i][0] = yoo[j][0];
                        yoo[j][0] = x;
                        change = true;
                    }
                    }
                }
            }

            if(change)
                change = false;
            else
                break;
        }

        for(long long i = 0; i < yoo.size(); i++ ) {
            //cout << yoo[i][0] << " " << yoo[i][1] << endl;
            total2[yoo[i][1]-yoo[i][0]]++;
        }
        long long difff = 0;
        //for(int i = 1; i < 7; i++ ) {
        //    cout << total2[i] << endl;
        //}
        for(int i = 1; i < 100; i++) {
            difff+= price(N, i) * (total1[i] - total2[i]);
        }
        cout << difff;

		cout << endl;
		data_num--;
		case_count++;
	}
	return 0;

}
