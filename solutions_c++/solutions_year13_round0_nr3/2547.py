//============================================================================
// Name        : task2.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdio>
#include <cstring>
#include <algorithm>
#include <limits>
#include <iostream>
#include <utility>
#include <fstream>

const int MAXD = 1005, DIG = 9, BASE = 1000000000;
const unsigned long long BOUND = std::numeric_limits<unsigned long long>::max() - (unsigned long long) BASE * BASE;

struct bignum
{
    int D;
    int digits [MAXD / DIG + 2];

    inline void trim ()
    {
        while (D > 1 && digits [D - 1] == 0)
            D--;
    }

    inline void init (long long x)
    {
        memset (digits, 0, sizeof (digits));
        D = 0;

        do
        {
            digits [D++] = x % BASE;
            x /= BASE;
        }
        while (x > 0);
    }

    inline bignum (long long x)
    {
        init (x);
    }

    inline bignum (int x = 0)
    {
        init (x);
    }

    inline bignum (const char *s, int l = -1)
    {
        memset(digits, 0, sizeof(digits));
        int len = l >= 0 ? l :strlen(s);
        int first = (len + DIG - 1) % DIG + 1;

        D = (len + DIG - 1) / DIG;

        for (int i = 0; i < first; i++)
            digits [D - 1] = digits [D - 1] * 10 + s [i] - '0';

        for (int i = first, d = D - 2; i < len; i += DIG, d--)
            for (int j = i; j < i + DIG; j++)
                digits [d] = digits [d] * 10 + s [j] - '0';

        trim ();
    }

    inline void tostr (char* buf, int* len, bool dotrim = true)
    {
    	if (dotrim)
    		trim();
        int pos = 0, d = digits [D - 1];

        do
        {
            buf [pos++] = d % 10 + '0';
            d /= 10;
        }
        while (d > 0);

        std::reverse (buf, buf + pos);

        for (int i = D - 2; i >= 0; i--, pos += DIG)
        {
            for (int j = DIG - 1, t = digits [i]; j >= 0; j--)
            {
                buf [pos + j] = t % 10 + '0';
                t /= 10;
            }
        }

        buf [pos] = '\0';
       	*len = pos;
    }

    inline char *str (int* len = 0)
    {
        trim ();
        char *buf = new char [DIG * D + 1];
        int l = 0;
        tostr(buf, &l, false);
        if (len)
        	*len = l;
        return buf;
    }

    inline bool operator < (const bignum &o) const
    {
        if (D != o.D)
            return D < o.D;

        for (int i = D - 1; i >= 0; i--)
            if (digits [i] != o.digits [i])
                return digits [i] < o.digits [i];

        return false;
    }

    inline bool operator == (const bignum &o) const
    {
        if (D != o.D)
            return false;

        for (int i = 0; i < D; i++)
            if (digits [i] != o.digits [i])
                return false;

        return true;
    }

    inline bignum operator << (int p) const
    {
        bignum temp;
        temp.D = D + p;

        for (int i = 0; i < D; i++)
            temp.digits [i + p] = digits [i];

        for (int i = 0; i < p; i++)
            temp.digits [i] = 0;

        return temp;
    }

    inline bignum operator >> (int p) const
    {
        bignum temp;
        temp.D = D - p;

        for (int i = 0; i < D - p; i++)
            temp.digits [i] = digits [i + p];

        for (int i = D - p; i < D; i++)
            temp.digits [i] = 0;

        return temp;
    }

    inline bignum range (int a, int b) const
    {
        bignum temp = 0;
        temp.D = b - a;

        for (int i = 0; i < temp.D; i++)
            temp.digits [i] = digits [i + a];

        return temp;
    }

    inline bignum operator + (const bignum &o) const
    {
        bignum sum = o;
        int carry = 0;

        for (sum.D = 0; sum.D < D || carry > 0; sum.D++)
        {
            sum.digits [sum.D] += (sum.D < D ? digits [sum.D] : 0) + carry;

            if (sum.digits [sum.D] >= BASE)
            {
                sum.digits [sum.D] -= BASE;
                carry = 1;
            }
            else
                carry = 0;
        }

        sum.D = std::max(sum.D, o.D);
        sum.trim ();
        return sum;
    }

    inline bignum operator - (const bignum &o) const
    {
        bignum diff = *this;

        for (int i = 0, carry = 0; i < o.D || carry > 0; i++)
        {
            diff.digits [i] -= (i < o.D ? o.digits [i] : 0) + carry;

            if (diff.digits [i] < 0)
            {
                diff.digits [i] += BASE;
                carry = 1;
            }
            else
                carry = 0;
        }

        diff.trim ();
        return diff;
    }

    inline bignum operator * (const bignum &o) const
    {
        bignum prod = 0;
        unsigned long long sum = 0, carry = 0;

        for (prod.D = 0; prod.D < D + o.D - 1 || carry > 0; prod.D++)
        {
            sum = carry % BASE;
            carry /= BASE;

            for (int j = std::max(prod.D - o.D + 1, 0); j <= std::min(D - 1, prod.D); j++)
            {
                sum += (unsigned long long) digits [j] * o.digits [prod.D - j];

                if (sum >= BOUND)
                {
                    carry += sum / BASE;
                    sum %= BASE;
                }
            }

            carry += sum / BASE;
            prod.digits [prod.D] = sum % BASE;
        }

        prod.trim ();
        return prod;
    }

    inline double double_div (const bignum &o) const
    {
        double val = 0, oval = 0;
        int num = 0, onum = 0;

        for (int i = D - 1; i >= std::max(D - 3, 0); i--, num++)
            val = val * BASE + digits [i];

        for (int i = o.D - 1; i >= std::max(o.D - 3, 0); i--, onum++)
            oval = oval * BASE + o.digits [i];

        return val / oval * (D - num > o.D - onum ? BASE : 1);
    }

    inline std::pair<bignum, bignum> divmod (const bignum &o) const
    {
        bignum quot = 0, rem = *this, temp;

        for (int i = D - o.D; i >= 0; i--)
        {
            temp = rem.range (i, rem.D);
            int div = (int) temp.double_div (o);
            bignum mult = o * div;

            while (div > 0 && temp < mult)
            {
                mult = mult - o;
                div--;
            }

            while (div + 1 < BASE && !(temp < mult + o))
            {
                mult = mult + o;
                div++;
            }

            rem = rem - (o * div << i);

            if (div > 0)
            {
                quot.digits [i] = div;
                quot.D = std::max(quot.D, i + 1);
            }
        }

        quot.trim ();
        rem.trim ();
        return std::make_pair(quot, rem);
    }

    inline bignum operator / (const bignum &o) const
    {
        return divmod(o).first;
    }

    inline bignum operator % (const bignum &o) const
    {
        return divmod(o).second;
    }

    inline bignum power (int exp) const
    {
        bignum p = 1;
        bignum temp = *this;

        while (exp > 0)
        {
            if (exp & 1)
            	p = p * temp;
            if (exp > 1)
            	temp = temp * temp;
            exp >>= 1;
        }

        return p;
    }

    inline void print()
    {
    	char* s = str();
    	std::cout << s;
    	delete s;
    }

    inline bignum d2(bignum& o)
    {
    	std::pair<bignum, bignum> dr = o.divmod(2);
    	bignum b = dr.first + (dr.second == 0 ? 0 : 1);
    	return b;
    }

    inline std::pair<bignum, bool> square()
    {
    	//std::cout << "SQ of ";
    	//print();
    	//std::cout << std::endl;

    	bignum b = *this;
    	bignum a = 1;

    	while (1)
    	{
    		bignum t = b - a;
    		if (t == 1)
    		{
    			//std::cout << "Nonperfect (small) sq = ";
    			//a.print();
    			//std::cout << std::endl;
    			return std::make_pair(a, false);
    		}

    	   	bignum c = a + t / 2;

    	   	//std::cout << "a = ";
    	   	//a.print();
    	   	//std::cout << " b = ";
    	   	//b.print();
    	   	//std::cout << " c = ";
    	   	//c.print();
    	   	//std::cout << std::endl;

    	   	bignum cc = c * c;

    	   	if (cc == *this)
    	   	{
    	   		//std::cout << "Perfect sq = ";
    	   		//c.print();
    	   		//std::cout << std::endl;
    	   		return std::make_pair(c, true);
    	   	}

    	   	if (*this < cc)
    	   		b = c;
    	   	else
    	   		a = c;
    	}

    	return std::make_pair(bignum(0), false);
    }
};

bool isPoly(bignum& o)
{
	static char buf[DIG * MAXD + 1];
	int len = 0;
	o.tostr(buf, &len);

	if (len % 2 == 0)
	{
		for (int b = 0, e = len - 1; b < e; b++, e--)
		{
			if (buf[b] != buf[e])
				return false;
		}
	}
	else
	{
		for (int b = 0, e = len - 1; b != e; b++, e--)
		{
			if (buf[b] != buf[e])
				return false;
		}
	}

	return true;
}

int cmpr(char * str1, char * str2, int len)
{
	char * str11 = str1 + len - 1;
	for(int k = 0; k < len; k++, str11--, str2++)
	{
		int diff = *str11 - *str2;
		if(diff != 0)
			return diff;
	}
	return 0;
}

bool incstr(char * str, int len)
{
	for(int n = len - 1; n >= 0; n--)
	{
		int c = str[n] - '0';
		if(c == 9)
		{
			str[n] = '0';
		}
		else
		{
			str[n] = c + 1 + '0';
			return false;
		}
	}
	return true;
}

bool isStrPoly(char* str, int len)
{
	int mid = len / 2;
	int center = len % 2;
	return 0 == cmpr(str, str + mid + center, mid);
}

void nextPalin(char *& str, int & len)
{
	int mid = len / 2;
	int center = len % 2;
	if(cmpr(str, str + mid + center, mid) <= 0)
	{
		if(incstr(str, mid + center))
		{
			str --;
			*str = '1';
			len ++;
			mid = len / 2;
			center = len % 2;
		}
	}
	for(int n = mid + center, k = mid - 1; n < len; n++, k--)
		str[n] = str[k];
}

int main()
{
	std::fstream f;
	f.open("1.in");

	int N = 0;
	f >> N;
	//std::cout << N;

	for (int n = 0; n < N; ++n)
	{
		std::string sa, sb;
		f >> sa;
		f >> sb;

		bignum a(sa.c_str(), sa.length());
		bignum b(sb.c_str(), sb.length());

		std::pair<bignum, bool> pma = a.square();
		bignum ma = pma.first;
		if (!pma.second)
			ma = ma + 1;
		bignum mb = b.square().first;

		static char megabuf[3000];
		int l = 0;
		ma.tostr(megabuf + 1000, &l, true);

		int tc = 0;
		char* pbuf = megabuf + 1000;
		while(1)
		{
			bignum b(pbuf);
			if (mb < b)
				break;

			if (isStrPoly(pbuf, l))
			{
				bignum bb = b * b;
				if (isPoly(bb))
				{
					//bb.print();
					//std::cout << std::endl;
					tc ++;
				}
			}

			nextPalin(pbuf, l);
		}

		std::cout << "Case #" << n + 1 << ": " << tc << std::endl;
	}

	return 0;
}


















