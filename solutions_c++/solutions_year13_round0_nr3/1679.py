#include <iostream>
#include <vector>

#define OUT_MAX 100000000000000
#define SUB_MAX 10000001

using namespace std;

typedef unsigned long long ullong;

ullong reverse(ullong num)
{
        ullong result = 0;
        while(num)
        {
                result = (result*10) + (num%10);
                num = num/10;
        }
	return result;
}

bool is_palindrome(ullong num)
{
	return (num == reverse(num));
}

int main()
{
	ullong T = 0;
	cin >> T;
	vector<ullong> list;
	for(ullong i=1;i<=SUB_MAX;i++)
	{
		if((i*i) > OUT_MAX) break;
		if(is_palindrome(i) && is_palindrome((i*i))) list.push_back(i*i);
	}
	//for (std::vector<ullong>::iterator it = list.begin() ; it != list.end(); ++it) std::cout << ' ' << *it; cout << endl;
	for(ullong t=1;t<=T;t++)
	{
		ullong A = 0, B = 0;
		cin >> A >> B;
		ullong cnt = 0;
		for (std::vector<ullong>::iterator it = list.begin() ; it != list.end(); ++it)
			if((*it) >= A && (*it) <= B)
				cnt++;
		cout << "Case #" << t << ": " << cnt << endl;
	}
	return 0;
}
