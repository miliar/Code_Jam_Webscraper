#include <cstdio>
#include <cfloat>
double best, cur, c, f, x, in, t;
int fc, tn, mfc;

int main()
{
    scanf("%d", &tn);
    for (int ti=1; ti<=tn; ++ti) {
        scanf("%lf%lf%lf", &c, &f, &x);
        in = 2.0;
        best = FLT_MAX;
        cur = x / in;
        fc = 0;
        t = 0;
        do {
            //printf("fc %d cur %.4lf best %.4lf\n", fc, cur, best);
            if (cur < best) best = cur;
            t += c / in; // czekamy na farme
            ++fc; // kupujemy
            in += f;
            cur = t + (x / in);
            //printf("  t %.4lf cur %.4lf\n", t, cur);
        } while (cur < best);
        //fprintf(stderr, "fc = %d\n", fc);
        if (fc > mfc) mfc = fc;
        printf("Case #%d: %.7lf\n", ti, best);
    }
    fprintf(stderr, "mfc = %d\n", mfc);
}
