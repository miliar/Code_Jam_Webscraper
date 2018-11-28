#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

enum QUATVAL
{
	QUATVAL_INVALID,
	QUATVAL_ONE,
	QUATVAL_I,
	QUATVAL_J,
	QUATVAL_K
};

class quat
{
public:
	quat() : val(QUATVAL_ONE), negative(false)
	{
	}

	quat(const char *v)
	{
		_makeval(v);
	}

	bool operator ==(const quat &other) const
	{
		return (val == other.val) && (negative == other.negative);
	}
	
	bool operator !=(const quat &other) const
	{
		return !(*this == other);
	}

	quat operator -(void)
	{
		quat result = *this;
		result.negative = !result.negative;
		return result;
	}

	quat &operator *=(const quat &other)
	{
		bool fn = negative != other.negative;
	
		if (val != QUATVAL_INVALID && other.val != QUATVAL_INVALID && other.val != QUATVAL_ONE)
		{
			if (val == QUATVAL_ONE)
				val = other.val, negative = false;
			else if (val == other.val)
				val = QUATVAL_ONE, negative = true;
			else if (val == QUATVAL_I && other.val == QUATVAL_J)
				val = QUATVAL_K, negative = false;
			else if (val == QUATVAL_J && other.val == QUATVAL_K)
				val = QUATVAL_I, negative = false;
			else if (val == QUATVAL_K && other.val == QUATVAL_I)
				val = QUATVAL_J, negative = false;
			else if (val == QUATVAL_J && other.val == QUATVAL_I)
				val = QUATVAL_K, negative = true;
			else if (val == QUATVAL_K && other.val == QUATVAL_J)
				val = QUATVAL_I, negative = true;
			else if (val == QUATVAL_I && other.val == QUATVAL_K)
				val = QUATVAL_J, negative = true;
		}

		negative ^= fn;
		return *this;
	}

	quat operator *(const quat &other) const
	{
		quat result = *this;
		result *= other;
		return result;
	}

private:
	void _makeval(const char *v)
	{
		char ch = '\0';

		if (v[0] == '-' && v[1] != '\0' && v[2] == '\0')
		{
			negative = true;
			ch = v[1];
		}
		else if (v[0] != '\0' && v[1] == '\0')
		{
			negative = false;
			ch = v[0];
		}

		switch (ch)
		{
		case '1' : val = QUATVAL_ONE; break;
		case 'i' : val = QUATVAL_I; break;
		case 'j' : val = QUATVAL_J; break;
		case 'k' : val = QUATVAL_K; break;
		default: val = QUATVAL_INVALID;
		}
	}

	char *_makecptr(char *out) const
	{
		char *p = out;

		if (negative)
			*p++ = '-';

		switch (val)
		{
		case QUATVAL_ONE: *p++ = '1'; break;
		case QUATVAL_I: *p++ = 'i'; break;
		case QUATVAL_J: *p++ = 'j'; break;
		case QUATVAL_K: *p++ = 'k';
		}
		*p++ = '\0';

		return out;
	}
	friend std::ostream &operator <<(std::ostream &os, const quat &q);
	friend std::istream &operator >>(std::istream &is, quat &q);
	QUATVAL val;
	bool negative;
};

std::ostream &operator <<(std::ostream &os, const quat &q)
{
	char out[3];
	q._makecptr(out);
	return (os << out);
}

std::istream &operator >>(std::istream &is, quat &q)
{

	char in[3] = {0};
	is >> in[0];
	if (in[0] == '-')
		is >> in[1];
	q = in;
	return is;
}

int main(void)
{
	//freopen("C-small-attempt2.in", "r", stdin);
	//freopen("C-small-attempt2.out", "w", stdout);
	int T; cin >> T;
	for (int v = 1; v <= T; v++)
	{
		int L, X;
		int count = 0;
		quat total = "1";
		vector<quat> vq;
		cin >> L >> X;
		for (int i = 0; i < L; i++)
		{
			quat q;
			cin >> q;
			vq.push_back(q);
		}

		for (int i = 0; i < X; i++)
			for (int j = 0; j < L; j++)
			{
				total *= vq[j];
				if ((count == 0 && total == "i") || 
					(count == 1 && total == "j"))
					total = "1", count++;
			}
		
		cout << "Case #" << v << ": " << (count == 2 && total == "k" ? "YES" : "NO" )<< endl;
	}

	return 0;
}
