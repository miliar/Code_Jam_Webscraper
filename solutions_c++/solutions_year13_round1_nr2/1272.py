#ifndef __GARBAGE_COLLECTOR_HELPER__
#define __GARBAGE_COLLECTOR_HELPER__

/* */
void rchar(char *c);
/* */
void r1int(unsigned *i0);
/* */
void r2int(unsigned *i1, unsigned *i2);
/* */
void r3int(unsigned *i0, unsigned *i1, unsigned *i2);
/* */
void r1double(double *d0);
/* */
void r2double(double *d1, double *i2);
/* */
void newtabint(unsigned **tab, unsigned nb_line, unsigned nb_col);
/* */
void newtabdouble(double **tab, unsigned nb_line, unsigned nb_col);

/* */
void dchar(char c);
/* */
void d1int(unsigned i0);
/* */
void d2int(unsigned i0, unsigned i1);
/* */
void d1double(double d0);
/* */
void d2double(double d0, double d1);
/* */
void dtabint(unsigned *tab, unsigned nb_line, unsigned nb_col);
/* */
void dtabdouble(double *tab, unsigned nb_line, unsigned nb_col);

#endif
