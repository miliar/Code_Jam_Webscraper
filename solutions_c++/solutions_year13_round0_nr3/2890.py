#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstring>
#include <sstream>

using namespace std;

const int SIZE=250;
struct hugeint {
	int len,num[SIZE];
	int remains;
};

long total [100];

hugeint times(hugeint a,hugeint b) {
	int i,j;
	hugeint ans;
	memset(ans.num,0,sizeof(ans.num));
	for (i=1;i<=a.len;i++)
		for (j=1;j<=b.len;j++)
			ans.num[i+j-1]+=a.num[i]*b.num[j];
	for (i=1;i<=a.len+b.len;i++) {
		ans.num[i+1]+=ans.num[i]/10;
		ans.num[i]=ans.num[i]%10;
	}
	if (ans.num[a.len+b.len]>0)
		ans.len=a.len+b.len;
	else
		ans.len=a.len+b.len-1;
	return ans;
}

hugeint add(hugeint a,hugeint b) {
	int i;
	hugeint ans;
	memset(ans.num,0,sizeof(ans.num));
	if (a.len>b.len)
		ans.len=a.len;
	else
		ans.len=b.len;
	for (i=1;i<=ans.len;i++) {
		ans.num[i]+=(a.num[i]+b.num[i]);
		ans.num[i+1]+=ans.num[i]/10;
		ans.num[i]%=10;
	}
	if (ans.num[ans.len+1]>0)
		ans.len++;
	return ans;
}

hugeint average(hugeint a,hugeint b) {
	int i;
	hugeint ans;
	ans=add(a,b);
	for (i=ans.len;i>=2;i--) {
		ans.num[i-1]+=(ans.num[i]%2)*10;
		ans.num[i]/=2;
	}
	ans.num[i]/=2;
	if (ans.num[ans.len]==0)
		ans.len--;
	return ans;
}

hugeint plustwo(hugeint a) {
	int i;
	hugeint ans;

	ans=a;
	ans.num[1]+=2;
	i=1;
	while ((i<=ans.len) && (ans.num[i]>=10) ) {
		ans.num[i+1]+=ans.num[i]/10;
		ans.num[i]%=10;
		i++;
	}
	if (ans.num[ans.len+1]>0)
		ans.len++;
	return ans;
}

bool over(hugeint a,hugeint b) {
	int i;
	if (a.len<b.len)
	return false;
	if (a.len>b.len)
	return true;
	for (i=a.len;i>=1;i--) {
		if (a.num[i]<b.num[i])
			return false;
		if (a.num[i]>b.num[i])
			return true;
	}
	return false;
}

bool diff (hugeint a,hugeint b) {
	int i;
	if (a.len != b.len) return true;
	for (i=a.len;i>=1;i--) {
		if (a.num[i] != b.num[i]) return true;
	}
	return false;
}

hugeint R (hugeint target) {
	hugeint left,middle,right;
	memset(left.num,0,sizeof(left.num));
	left.len=1;
	left.num[1]=1;
	right=target;
	hugeint sp;
	do {
		middle=average(left,right);
		sp=times(middle,middle);
		if (over (sp, target))
			right=middle;
		else
			left=middle;
	} while (!over(plustwo(left),right));
	sp = times (left, left);
	if (diff (target, sp)) left.remains = 1;
	else left.remains = 0;
	return left;
}

class FileReader : public ifstream {
public:
    FileReader( const string& filename ) { open( filename.c_str(), ios_base::in ); }
    int readInt() { int x = 0; *this >> x; return x; }
    vector<int> readInts( int n ) { vector<int> v(n); for ( int i = 0; i < n; i++ ) v[i] = readInt(); return v; }
    string readLine() { char buf[20000]; getline( buf, sizeof(buf) ); return buf; }
    string readString() { string x; *this >> x; return x; }
    vector<string> readStrings( int n ) { vector<string> v; for ( int i = 0; i < n; i++ ) v.push_back( readString() ); return v; }
    __int64 readInt64() { __int64 x; *this >> x; return x; }
};

class FileWriter : public ofstream {
public:
    FileWriter( const string& filename ) { open( filename.c_str(), ios_base::out ); }
};

__int64 gcd( __int64 a, __int64 b ) { return a ? gcd( b%a, a ) : b; }

long C (long a, long b) {
    long x = 1;
    for (int i = 0; i < b; i ++) {
        x *= a - i;
        x /= i + 1;
    }
    return x;
}

long trim (hugeint T) {
    if (T.len == 1) {
        if (T.num [1] >= 3) return 3;
        if (T.num [1] == 2) return 2;
        return 1;
    }
    if (T.num [T.len] > 2) return total [T.len];
    int i;
    hugeint tmp;
    memset(tmp.num,0,sizeof(tmp.num));
    if (T.num [T.len] == 2) {
        tmp.len = T.len;
        tmp.num [1] = tmp.num [tmp.len] = 2;
        if (tmp.len % 2) {
            i = 2;
            while (i <= tmp.len / 2) { tmp.num [i] = tmp.num [tmp.len - i + 1] = 0; i ++; }
            tmp.num [i] = 1;
            if (!over (tmp, T)) return total [T.len];
            tmp.num [i] = 0;
            if (!over (tmp, T)) return total [T.len] - 1; else return total [T.len] - 2;
        } else {
            i = 2;
            while (i <= tmp.len / 2) { tmp.num [i] = tmp.num [tmp.len - i + 1] = 0; i ++; }
            if (!over (tmp, T)) return total [T.len]; else return total [T.len] - 1;
        }
    } else {
        int k, a [3], ai;
        int cnt = 0;
        tmp.len = T.len;
        tmp.num [1] = tmp.num [tmp.len] = 1;
        k = tmp.len / 2;
        if (tmp.len % 2) {
            i = 2;
            ai = 0;
            while (i <= tmp.len / 2) {
                if (T.num [T.len - i + 1] == 1) {
                    if (ai < 3) a [ai] = k - i;
                    ai ++;
                    tmp.num [tmp.len - i + 1] = tmp.num [i] = 1;
                } else if (T.num [T.len - i + 1] == 0) tmp.num [tmp.len - i + 1] = tmp.num [i] = 0;
                else {
                    a [ai] = k - i;
                    ai ++;
                    if (ai > 1) cnt = 2; else cnt = 3;
                    if (ai > 2) cnt += C (a [2], 1) + 1;
                    if (ai > 1) cnt += C (a [1], 2) + C (a [1], 1) + 1;
                    cnt += C (a [0], 3) + C (a [0], 2) + C (a [0], 1) + 1;
                    return cnt;
                }
                i ++;
            }
            if (ai > 3) cnt = 2;
            else if (ai == 3 || ai == 2) {
                tmp.num [i] = 1;
                if (!over (tmp, T)) cnt = 2;
                else {
                    tmp.num [i] = 1;
                    if (!over (tmp, T)) cnt = 1; else cnt = 0;
                }
            } else if (ai == 1) {
                tmp.num [i] = 2;
                if (!over (tmp, T)) cnt = 3;
                else {
                    tmp.num [i] = 1;
                    if (!over (tmp, T)) cnt = 2;
                    else {
                        tmp.num [i] = 0;
                        if (!over (tmp, T)) cnt = 1; else cnt = 0;
                    }
                }
            }
            if (ai > 2 ) cnt += C (a [2], 1) * 2 + 2;
            if (ai > 1 ) cnt += (C (a [1], 2) + C (a [1], 1)) * 2 + 3;
            if (ai > 0 ) cnt += (C (a [0], 3) + C (a [0], 2)) * 2 + C (a [0], 1) * 3 + 3;
            return cnt;
        } else {
            i = 2;
            ai = 0;
            while (i <= tmp.len / 2) {
                if (T.num [T.len - i + 1] == 1) {
                    if (ai < 3) a [ai] = k - i;
                    ai ++;
                    tmp.num [tmp.len - i + 1] = tmp.num [i] = 1;
                } else if (T.num [T.len - i + 1] == 0) tmp.num [tmp.len - i + 1] = tmp.num [i] = 0;
                else {
                    a [ai] = k - i;
                    ai ++;
                    cnt = 1;
                    if (ai > 2 ) cnt += C (a [2], 1) + 1;
                    if (ai > 1 ) cnt += C (a [1], 2) + C (a [1], 1) + 1;
                    cnt += C (a [0], 3) + C (a [0], 2) + C (a [0], 1) + 1;
                    return cnt;
                }
                i ++;
            }
            if (ai > 3 || !over (tmp, T)) cnt = 1; else cnt = 0;
            if (ai > 2 ) cnt += C (a [2], 1) + 1;
            if (ai > 1 ) cnt += C (a [1], 2) + C (a [1], 1) + 1;
            if (ai > 0 ) cnt += C (a [0], 3) + C (a [0], 2) + C (a [0], 1) + 1;
            return cnt;
        }
    }
}

int main() {
    FileReader fin( "C-small-attempt1.in" );
    FileWriter fout( "out.txt" );

    memset(total,0,sizeof(total));
    total [1] = 3;
    for (int i = 2; i < 100; i ++)
        cout << (total [i] = (i % 2) ? ((i * i * i - 9 * i * i + 59 * i - 3) / 24) : ((i * i * i - 6 * i * i + 32 * i) / 48 + 1)) << ' ';
    cout << endl;

    int caseCount;
    fin >> caseCount;
    fin.readLine();
    for (int cc = 0; cc < caseCount; cc ++ ) {
        string s;
        hugeint L, H, Lr, Hr;
        s = fin.readLine();
        memset(L.num,0,sizeof(L.num));
        memset(Lr.num,0,sizeof(Lr.num));
        memset(H.num,0,sizeof(H.num));
        memset(Hr.num,0,sizeof(Hr.num));
        L.len = s.find(' ');
        H.len = s.length() - L.len - 1;
        int i;
        for (i = 1; i <= L.len; i ++) L.num [i] = s [L.len - i] - '0';
        Lr = R (L);
        for (i = 1; i <= H.len; i ++) H.num [i] = s [s.length() - i] - '0';
        Hr = R (H);

        long sumL = 0;
        i = 1;
        while (i < Lr.len) {
            sumL += total [i];
            i ++;
        }
        long sumH = sumL;
        while (i < Hr.len) {
            sumH += total [i];
            i ++;
        }
        cout << L.len << ' ' << H.len << ';' << endl;
        cout << sumL << ' ' << sumH << endl;
        sumL += trim (Lr);
        sumH += trim (Hr);
        cout << sumL << ' ' << sumH << endl;
        if (Lr.remains == 0) {
            sumL --;
            i = 1;
            while (i <= Lr.len / 2) {
                if (Lr.num[i] != Lr.num [Lr.len - i + 1]) {
                    sumL ++;
                    break;
                }
                i ++;
            }
        }

        stringstream ss;
        ss << "Case #" << cc + 1 << ": " << sumH - sumL << endl;
        fout << ss.str().c_str();
        cout << ss.str().c_str();
    }
    return 0;
}
