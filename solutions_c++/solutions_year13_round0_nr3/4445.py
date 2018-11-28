#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>

class Bignum {
	public:
		char data[102];
		int digit;

		Bignum()
		{
			for (int i = 0; i < 102; i++)
			{
				this->data[i] = 0;
			}
			this->digit = 1;
		}

		Bignum(const char *num)
		{
			for (int i = 0; i < 102; i++)
			{
				this->data[i] = 0;
			}

			this->digit = strlen(num);
			for (int i = 0; i < digit; i++)
			{
				this->data[i] = num[digit - i - 1] - '0';
			}
		}

		char* to_str()
		{
			char *s;

			s = (char *) calloc(this->digit, sizeof(char));
			for (int i = 0; i < digit; i++)
			{
				s[i] = this->data[digit - i - 1] + '0';
			}
			s[digit] = 0;

			return s;
		}

		// Comparision
		bool is_palindrome()
		{
			int i, j;

			for (i = 0, j = digit - 1; i < j; i++, j--)
			{
				if (this->data[i] != this->data[j])
				{
					return false;
				}
			}

			return true;
		}

		bool is_gt(Bignum *b)
		{
			if (this->digit != b->digit)
			{
				return (this->digit > b->digit) ? true : false;
			}
			else
			{
				for (int i = this->digit - 1; i >= 0; i--)
				{
					if (this->data[i] != b->data[i])
					{
						return (this->data[i] > b->data[i]) ? true : false;
					}
				}

				return false;
			}
		}

		bool is_gte(Bignum *b)
		{
			if (this->digit != b->digit)
			{
				return (this->digit > b->digit) ? true : false;
			}
			else
			{
				for (int i = this->digit - 1; i >= 0; i--)
				{
					if (this->data[i] != b->data[i])
					{
						return (this->data[i] > b->data[i]) ? true : false;
					}
				}

				return true;
			}
		}

		bool is_lte(Bignum *b)
		{
			return !is_gt(b);
		}

		bool is_lt(Bignum *b)
		{
			return !is_gte(b);
		}

		bool is_eq(Bignum *b)
		{
			return !is_gt(b) && is_gte(b);
		}

		// Operations
		Bignum* add(Bignum *b)
		{
			Bignum *tmp;
			int i, digit;
			int r = 0;

			tmp = new Bignum();
			digit = (this->digit > b->digit) ? this->digit : b->digit;
			tmp->digit = digit;

			for (i = 0; i < digit; i++)
			{
				tmp->data[i] = this->data[i] + b->data[i] + r;
				r = tmp->data[i] / 10;
				tmp->data[i] %= 10;
			}

			if (r > 0)
			{
				tmp->data[digit] = r;
				tmp->digit = digit + 1;
			}

			return tmp;
		}

		Bignum* mult(Bignum *b)
		{
			Bignum *tmp1, *tmp2;
			int i, j;
			int r;

			tmp1 = new Bignum("0");

			for (i = 0; i < b->digit; i++)
			{
				if (b->data[i] == 0)
				{
					continue;
				}

				tmp2 = new Bignum();
				tmp2->digit = i;
				r = 0;

				for (j = 0; j < this->digit; j++)
				{
					tmp2->data[j + i] = this->data[j] * b->data[i] + r;
					r = tmp2->data[j + i] / 10;
					tmp2->data[j + i] %= 10;
					(tmp2->digit)++;
				}

				if (r > 0)
				{
					tmp2->data[j + i] = r;
					(tmp2->digit)++;
				}

				tmp1 = tmp1->add(tmp2);
			}

			return tmp1;
		}
};

int main()
{
	int case_total, case_current;
	Bignum *num1, *num2, *t;
	char n1[102], n2[102];
	Bignum *lb, *ub;
	Bignum *lbq, *ubq;
	Bignum *count;

	scanf("%d", &case_total);

	for (case_current = 1; case_current <= case_total; case_current++)
	{
		scanf("%s %s", n1, n2);
		num1 = new Bignum(n1);
		num2 = new Bignum(n2);
		count = new Bignum("0");

		lb = new Bignum();
		lb->digit = floor((num1->digit - 1) / 2.0) + 1;
		lb->data[lb->digit - 1] = 1;
		/*ub = new Bignum();
		ub->digit = floor((num2->digit - 1) / 2.0) + 2;
		ub->data[ub->digit - 1] = 1;*/
		lbq = lb->mult(lb);

		while (lbq->is_lt(num1))
		{
			lb = lb->add(new Bignum("1"));
			lbq = lb->mult(lb);
		}

		while (lbq->is_lte(num2))
		{
			if (lbq->is_palindrome() && lb->is_palindrome())
			{
				count = count->add(new Bignum("1"));
			}
			lb = lb->add(new Bignum("1"));
			lbq = lb->mult(lb);
		}

		printf("Case #%d: %s\n", case_current, count->to_str());
	}

	return 0;
}
