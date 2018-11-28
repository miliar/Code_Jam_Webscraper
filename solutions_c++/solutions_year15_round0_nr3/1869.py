#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

struct quaternion {
    int coord, sign;
    quaternion(int coord, int sign) : coord(coord), sign(sign) { }
    explicit quaternion(char c) : coord(c - 'i' + 1), sign(1) {} 
    
    quaternion operator*(const quaternion& q) const {
	if (coord == 0 || q.coord == 0)
	    return quaternion(coord + q.coord, sign*q.sign);
	if (q.coord == coord)
	    return quaternion(0, -sign*q.sign);

	int new_sign = q.coord - coord;
	if (abs(new_sign) != 1)
	    new_sign = -new_sign/2;

	return quaternion(6 - q.coord - coord, new_sign * sign * q.sign);
    }
    
    bool operator==(const quaternion& q) const {
	return coord == q.coord && sign == q.sign;
    }
};

quaternion eval(string str, long long times) {
    quaternion ret(0, 1);
    for (int z = 0; z < times%4; z++) 
	for (int i = 0; i < str.size(); i++)
	    ret = ret * quaternion(str[i]);
    return ret;
}

int substr_eq(string str, quaternion q, bool rev) {
    quaternion temp(0, 1);
    if (temp == q)
	return 0;
    
    for (int i = 0; i < str.size(); i++) {
	if (rev)
	    temp = quaternion(str[i]) * temp;
	else
	    temp = temp * quaternion(str[i]);
	
	if (temp == q)
	    return i+1;
    }

    return 0x3f3f3f3f;
}

int main() {
    int t;
    cin >> t;

    for (int z = 1; z <= t; z++) {
	long long L, X;
	string str;
	cin >> L >> X >> str;
	
	string expanded_str = str + str + str + str;
	assert(eval(expanded_str, 1) == quaternion(0, 1));
	
	int len_left = substr_eq(expanded_str, quaternion('i'), false);
	reverse(expanded_str.begin(), expanded_str.end());
	int len_right = substr_eq(expanded_str, quaternion('k'), true);

	cout << "Case #" << z << ": ";
	if (len_left + len_right <= L*X && eval(str, X) == quaternion(0, -1))
	    cout << "YES" << endl;
	else
	    cout << "NO" << endl;
    }
}
