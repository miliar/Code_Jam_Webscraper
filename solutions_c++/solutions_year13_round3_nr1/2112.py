# include <iostream>
using namespace std;

#define MAXLEN 1000005

char name[MAXLEN];
int n, len, nsub, sub[MAXLEN], sublen[MAXLEN];

# define isVowel(c) ((c) == 'a' || (c) == 'e' || (c) == 'i' || (c) == 'o' || (c) == 'u')

int countsub()
{
	int i, cnt, index, nsub;
	//memset(sub, -1, len * sizeof (int));
	//memset(sublen, 0, len * sizeof (int));
	cnt = nsub = 0;
	index = -1;
	for (i = 0; i < len; ++i) {
		if (!isVowel(name[i])) {
			if (index == -1)
				index = i;
			++cnt;
		}
		else if (index != -1) {
			if (cnt >= n) {
				sub[nsub] = index;
				sublen[nsub] = cnt;
				++nsub;
			}
			index = -1;
			cnt = 0;
		}

	}
	if (index != -1 && cnt >= n) {
		sub[nsub] = index;
		sublen[nsub] = cnt;
		++nsub;
	}
	return nsub;
}

int main()
{
	int T, iCase;
    scanf("%d", &T);
    for(iCase = 1; iCase <= T; ++iCase) {
		int ans, i, pre;
        cin >> name >> n;
		len = strlen(name);
		nsub = countsub();
		ans = 0;
		pre = 0;
		for (i = 0; i < nsub; ++i) {
			int cnt = len - sub[i] - n + 1;
			ans += (sub[i] - pre + 1) * cnt;
			pre = sub[i] + sublen[i] - n + 1;
			while (sublen[i]-- > n)
				ans += --cnt;
		}
		/*if (nsub > 0) {
		int isub = 0;
		for (i = 0; i < len; ++i) {
			if (i > sub[isub] && i > sub[isub] + sublen[isub] - n)
				if (++isub >= nsub)
					break;
			ans += len - sub[isub] - n + 1;
		}
		}*/
		printf("Case #%d: ", iCase);
		cout << ans << endl;
//		ans=0;
    }
    return 0;
}